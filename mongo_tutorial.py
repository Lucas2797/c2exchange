import pymongo
from pymongo import MongoClient



cluster = MongoClient("mongodb+srv://lucasrf27:lukasfaria@cluster0.bg4ur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["c2exchange"]
collection = db["Investiments"]

post = {"wallet":1, "coin":1, "ammount":5.0, "payd":4.2, "sold":False}


print(collection.find({"wallet": 1, "_id":0}))

for r in collection.find({"_id":0}):
    print(r)
    