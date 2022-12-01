from pymongo import MongoClient

client = MongoClient('ac-7fsmqnr-shard-00-02.oo5qzlu.mongodb.net:27017',
                     username='jchild2008',
                     password='bbcec4566',
                     authSource='admin',
                     authMechanism='SCRAM-SHA-1')

client.server_info()