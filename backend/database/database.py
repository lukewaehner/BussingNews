from pymongo import MongoClient, UpdateOne
from dotenv import load_dotenv
import os


def insertarticles(articles):
    load_dotenv('.env')
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db = client["BussingNews"]
    collection = db["newsarticles"]

    # Prepare bulk update operations
    operations = [
        UpdateOne({"url": article["url"]}, {"$set": article}, upsert=True) for article in articles
    ]

    # Execute bulk operation
    result = collection.bulk_write(operations)

    print(f"Inserted/Updated {result.upserted_count} articles.")
    client.close()
