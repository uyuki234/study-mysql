from pymongo import MongoClient

uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("ローカルMongoDBへの接続に成功しました。")
except Exception as error:
    print(error)
finally:
    client.close()
