import os
from dotenv import load_dotenv
from src.load_csv_to_mongodb import load_csv_to_mongodb
from src.llm_query_generator import generate_mongodb_query
from src.data_retriever import execute_query_and_save

def main():
    load_dotenv()
    #  Load CSV
    load_csv_to_mongodb('data/sample_data.csv', 'product_db', 'products')

    # Interactive loop
    while True:
        req = input("\nEnter your data request (or 'exit' to quit):\n> ")
        if req.lower() in ('exit', 'quit'):
            break

        # Generate
        try:
            query_json = generate_mongodb_query(req)
        except Exception as e:
            print(f"[!] LLM error: {e}")
            continue

        print(f"\n[Generated Query]:\n{query_json}\n")

        # Log query
        os.makedirs('queries', exist_ok=True)
        with open('queries/queries_generated.txt', 'a') as f:
            f.write(f"Request: {req}\nQuery: {query_json}\n\n")

        # Save or display
        choice = input("Type 'save' to CSV or 'show' to display results: ").strip().lower()
        if choice == 'show':
            from pandas import DataFrame
            import pandas as pd
            import ast
            data = ast.literal_eval(query_json)
            from pymongo import MongoClient
            client = MongoClient(os.getenv('MONGO_URI','mongodb://localhost:27017/'))
            docs = list(client['product_db']['products'].find(data))
            for d in docs:
                d.pop('_id', None)
            print(pd.DataFrame(docs))
            continue

        out = input("Enter output CSV path (e.g. outputs/test_case1.csv): ").strip()
        os.makedirs(os.path.dirname(out), exist_ok=True)

        #Execute & save
        try:
            execute_query_and_save(query_json, 'product_db', 'products', out)
        except Exception as e:
            print(f"[!] Retrieval error: {e}")

    print("Goodbye!")

if __name__ == "__main__":
    main()
