from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://jchild2008:bbcec4566@cluster0.oo5qzlu.mongodb.net/book?retryWrites=true&w=majority"
)
db = client.book

db.cats.delete_one({"name": "kuzia"})
result = db.cats.find_one({"name": "kuzia"})
print(result)