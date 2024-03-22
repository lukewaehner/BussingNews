from pymongo import MongoClient
from dotenv import load_dotenv
import os


def insertarticles(articles):
    load_dotenv('../.env')
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db = client["BussingNews"]
    collection = db["newsarticles"]

    for article in articles:
        # Using update_one with upsert=True to avoid duplication
        collection.update_one({"url": article["url"]}, {
                              "$set": article}, upsert=True)
    print(f"Inserted/Updated {len(articles)} articles.")

    client.close()
