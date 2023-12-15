from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
uri = os.environ["MONGODB_CONN"]

client = MongoClient(uri, tlsCAFile=certifi.where())

db = client.prode

users_collection = db["users"]
