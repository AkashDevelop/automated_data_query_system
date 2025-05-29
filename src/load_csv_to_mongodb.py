import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def load_csv_to_mongodb(csv_path: str, db_name: str, collection_name: str):
    df = pd.read_csv(csv_path)

    # Clean Discount column
    if 'Discount' in df.columns:
        df['Discount'] = df['Discount'].str.rstrip('%').astype(float)

    # Parse dates
    if 'LaunchDate' in df.columns:
        df['LaunchDate'] = pd.to_datetime(df['LaunchDate'], dayfirst=True)

    # To records
    data = df.to_dict(orient='records')

    # Connect
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    client = MongoClient(mongo_uri)
    coll = client[db_name][collection_name]

    # Reset & insert
    coll.drop()
    coll.insert_many(data)
    print(f"[+] Loaded {len(data)} documents into {db_name}.{collection_name}")