from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://jchild2008:bbcec4566@cluster0.oo5qzlu.mongodb.net/book?retryWrites=true&w=majority"
)
db = client.book

result = db.cats.find({})
for el in result:
    print(el)