from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('.env')
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client["BussingNews"]
collection = db["newsarticles"]


collection.delete_many({})
