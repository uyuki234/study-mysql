from pymongo import MongoClient

# ローカルMongoDBへ接続する
client = MongoClient("mongodb://127.0.0.1:27017/")

# データベースとコレクションを指定する
db = client["mydatabase"]
collection = db["mycollection"]

# 削除する商品名を入力する
name = input("name--> ")

# nameが一致する最初のドキュメントを削除する
result = collection.delete_one({"name": name})

# 結果を表示する
print("削除件数:", result.deleted_count)

client.close()
