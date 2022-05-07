import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://thw990210:<password>@cluster0.u4yhm.mongodb.net/UI?retryWrites=true&w=majority")
db = client.UI
collection = db.user_info
requesting = []

with open("./data/characters.json") as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

client.close()
