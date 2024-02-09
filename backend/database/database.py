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

document = {"name": "John Doe", "age": 25, "email": "test@example.com"}

insert_result = collection.insert_one(document)
print(f"Document inserted with _id: {insert_result.inserted_id}")

client.close()
# Now you can use `db` to interact with your database
