import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://jchild2008:bbcec4566@cluster0.oo5qzlu.mongodb.net/?retryWrites=true&w=majority"
      #     mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")