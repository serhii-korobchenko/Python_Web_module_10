
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace <connection string> with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://jchild2008:bbcec4566@cluster0.oo5qzlu.mongodb.net/?retryWrites=true&w=majority"

# Set the Stable API version on the client.
client = MongoClient(conn_str, server_api=ServerApi('1'), serverSelectionTimeoutMS=5000)
client.server_info()
