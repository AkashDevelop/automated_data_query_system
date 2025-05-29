import os
import pandas as pd
from pymongo import MongoClient
import ast

def execute_query_and_save(
    query_str: str,
    db_name: str,
    collection_name: str,
    output_csv: str
):
    try:
        query = ast.literal_eval(query_str)
    except Exception as e:
        raise ValueError(f"Failed to parse query JSON: {e}")

    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    client = MongoClient(mongo_uri)
    coll = client[db_name][collection_name]

    docs = list(coll.find(query))
    if not docs:
        print("No documents matched the query.")

    # Remove _id
    for d in docs:
        d.pop("_id", None)

    df = pd.DataFrame(docs)
    df.to_csv(output_csv, index=False)
    print(f"[+] Saved {len(df)} records to {output_csv}")
