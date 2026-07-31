from pymongo import MongoClient

# ローカルMongoDBへ接続する
client = MongoClient("mongodb://127.0.0.1:27017/")

# データベースとコレクションを指定する
db = client["mydatabase"]
collection = db["mycollection"]

# ドキュメントを登録する
collection.insert_one({
    "name": "リンゴ",
    "price": 100
})

collection.insert_one({
    "name": "ミカン",
    "price": 200,
    "area": "愛媛県"
})

collection.insert_one({
    "name": "バナナ",
    "price": 300
})

print(collection.count_documents({}))

client.close()
