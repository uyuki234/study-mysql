# sqlite3モジュールをインポートする
import sqlite3
# 検索する氏名をキー入力する
name = input("検索する氏名-->")
# データベースに接続してコネクションオブジェクトを取得する
con = sqlite3.connect("sample.db")
# カーソルオブジェクトを取得する
cur = con.cursor()
# SQL文を完成させて実行する
cur.execute("SELECT name, salary FROM Employee WHERE name LIKE ?", (name,))

# (name,)はタプル。カンマがないとただの値になってしまうので、カンマをつける

# 検索結果を表示する
print(cur.fetchall())
# カーソルを閉じる
cur.close()
# 接続を閉じる
con.close()
