# sqlite3モジュールをインポートする
import sqlite3

# 登録するレコードをキー入力する
emp_id = input("登録する社員ID-->")
name = input("登録する氏名-->")
gender = input("登録する性別-->")
salary = input("登録する給与-->")
birtyday = input("登録する生年月日-->")
dep_id = input("登録する部署ID-->")

# データベースに接続してコネクションオブジェクトを取得する
con = sqlite3.connect("sample.db")
# カーソルオブジェクトを取得する
cur = con.cursor()
# SQL文を完成させて実行する
cur.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?)", (emp_id, name, gender, salary, birtyday, dep_id))

# 登録をコミットする
con.commit()
# カーソルを閉じる
cur.close()
# 接続を閉じる
con.close()

# E007, 日経美子, F, 300000, 2001-03-03, D1