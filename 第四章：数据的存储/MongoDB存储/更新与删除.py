import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.game
collection = db.players

result = collection.update_one({'name': 'Ava'}, {'$set': {'age': 36}})
print(result)
print(result.matched_count, result.modified_count)  # int
result = collection.update_many({'age': 36}, {'$set': {'age': 27}})
print(result)

result = collection.delete_one({'name': 'anapple'})
print(result)
print(result.deleted_count)  # int
result = collection.delete_many({'name': 'anapple'})
print(result)
print(result.deleted_count)
