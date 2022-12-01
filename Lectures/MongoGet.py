from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://jchild2008:bbcec4566@cluster0.oo5qzlu.mongodb.net/book?retryWrites=true&w=majority"
)

db = client.book

result = db.cats.find_one({"_id": ObjectId("6388742f154180a9b674a2ae")})
print(result)