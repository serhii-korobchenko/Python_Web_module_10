import pymongo

client = pymongo.MongoClient("mongodb://jchild2008:bbcec4566@ac-tvwz7d7-shard-00-00.zbr1m79.mongodb.net:27017,ac-tvwz7d7-shard-00-01.zbr1m79.mongodb.net:27017,ac-tvwz7d7-shard-00-02.zbr1m79.mongodb.net:27017/?ssl=true&replicaSet=atlas-fata5n-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.server_info()
