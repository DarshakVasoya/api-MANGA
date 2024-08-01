
import urllib.parse
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import motor.motor_asyncio
import asyncio
def connecting_mongodb():
    # Your raw username and password
    raw_username = "darshakmainz"
    raw_password = "Darshak1310@"

    # URL-encode the username and password
    encoded_username = urllib.parse.quote_plus(raw_username)
    encoded_password = urllib.parse.quote_plus(raw_password)

    # Construct the MongoDB URI
    uri = f"mongodb+srv://{encoded_username}:{encoded_password}@manga.tu41ccq.mongodb.net/?retryWrites=true&w=majority"

    database_name = "manga"
    collection_name = "all_manga"

    # Create an instance of the MongoDB client
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client[database_name]
    collection = db[collection_name]

    # Connect to MongoDB
    client = MongoClient(uri, server_api=ServerApi('1'))
    return collection


