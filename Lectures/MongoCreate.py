import pprint

from pymongo import MongoClient


client = MongoClient("mongodb+srv://jchild2008:bbcec4566@cluster0.oo5qzlu.mongodb.net/?retryWrites=true&w=majority")
#db = client.test


db = client.book

collection = db.test_collection
print(collection)

# find_one = db.cats.find_one({"name": "Lama"})
# print(find_one)


#
# result_one = db.cats.insert_one(
#     {
#         "name": "kuzia",
#         "age": 3,
#         "features": ["ходит в тапки", "дает себя гладить", "рыжий"]
#     }
# )
#
# print(result_one.inserted_id)
#
# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходит в лоток", "не дает себя гладить", "серый"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходит в лоток", "дает себя гладить", "белый"],
#         },
#     ]
# )
# print(result_many.inserted_ids)