import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://jchild2008:bbcec4566@cluster0.zbr1m79.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.server_info()
