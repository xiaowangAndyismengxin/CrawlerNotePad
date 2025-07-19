import pymongo
from bson.objectid import ObjectId


# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client['game']
db = client.game
collection = db.players
student = {"_id": ObjectId("67a86ebd312cc3b6720d0657"), "name": "Aim", "age": 34}
result = collection.insert_one(student)
print(result.inserted_id)  # <class 'bson.objectid.ObjectId'>
students = [
    {"name": "Emma", "age": 28},
    {"name": "Liam", "age": 32},
    {"name": "Olivia", "age": 24},
    {"name": "Noah", "age": 19},
    {"name": "Ava", "age": 37},
    {"name": "Isabella", "age": 22},
    {"name": "Sophia", "age": 41},
    {"name": "Jackson", "age": 29},
    {"name": "Aiden", "age": 35},
    {"name": "Lucas", "age": 26},
    {"name": "Mia", "age": 31},
    {"name": "Ethan", "age": 18},
    {"name": "Harper", "age": 23},
    {"name": "Evelyn", "age": 39},
    {"name": "Benjamin", "age": 27},
]
result = collection.insert_many(students)
print(result.inserted_ids)  # list
