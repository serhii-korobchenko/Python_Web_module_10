import certifi
import pymongo

client = pymongo.MongoClient("mongodb+srv://jchild2008:bbcec4566@cluster0.zbr1m79.mongodb.net/test?retryWrites=true&w=majority")
db = client.server_info()
#server = client.server_info()
print(db)