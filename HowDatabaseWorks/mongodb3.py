from pymongo import MongoClient

# ローカルMongoDBへ接続する
client = MongoClient("mongodb://127.0.0.1:27017/")

# データベースとコレクションを指定する
db = client["mydatabase"]
collection = db["mycollection"]

# 書き換える商品名と価格を入力する
name = input("name--> ")
price = int(input("price--> "))

# nameが一致する最初のドキュメントを書き換える
result = collection.update_one(
    {"name": name},
    {"$set": {"price": price}}
)

# 結果を表示する
print("該当件数:", result.matched_count)
print("更新件数:", result.modified_count)

client.close()
