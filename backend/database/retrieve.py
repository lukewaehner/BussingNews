from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('./db.env')
# Replace the URI string with your connection string
username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")
database_name = os.environ.get("MONGO_DATABASE_NAME")

uri = f"mongodb+srv://{username}:{password}@newscluster.aemxbgw.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

# Select your database
db = client[database_name]

collection = db["newsdatacollection"]

documents = collection.find()

for doc in documents:
    print(doc)
