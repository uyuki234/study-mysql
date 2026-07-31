from pymongo import MongoClient

# ローカルMongoDBへ接続する
client = MongoClient("mongodb://127.0.0.1:27017/")

# データベースとコレクションを指定する
db = client["mydatabase"]
collection = db["mycollection"]

# 検索する商品名を入力する
name = input("name--> ")

# nameが一致する最初のドキュメントを検索する
document = collection.find_one({"name": name})

# 検索結果を表示する
print(document)

# 接続を閉じる
client.close()
