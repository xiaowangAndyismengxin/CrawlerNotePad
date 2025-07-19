import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.game
collection = db.players

result = collection.find_one({"age": 26})
print(result)  # dict

# 游标在遍历时会重新访问数据库，获取最新的数据
result = collection.find({"name": {"$regex": "^a", "$options": "i"}})
print(result)
# 在 MongoDB 中，游标（Cursor）是一个 单向迭代器，
# 默认情况下只能从头到尾遍历一次。一旦遍历完成，
# 游标就会耗尽（exhausted），无法再重新遍历。
for document in result:
    print(document)

# 精确
print(collection.count_documents({"name": {"$regex": "^a", "$options": "i"}}))  # int
# 粗略, 不支持查询
print(collection.estimated_document_count())  # int

result = collection.find({}).sort("name", pymongo.ASCENDING).limit(4)  # 1
print([doc["name"] for doc in result])
result = collection.find({}).sort("name", pymongo.DESCENDING).skip(1).limit(4)  # -1
print([doc["name"] for doc in result])
