# sqlite3モジュールをインポートする
import sqlite3

# 更新するレコードの社員IDと給与をキー入力する
emp_id = input("更新する社員ID-->")
salary = input("更新する給与-->")

# データベースに接続してコネクションオブジェクトを取得する
con = sqlite3.connect("sample.db")
# カーソルオブジェクトを取得する
cur = con.cursor()
# SQL文を完成させて実行する
cur.execute("UPDATE Employee SET salary = ? WHERE emp_id = ?", (salary, emp_id))

# 更新をコミットする
con.commit()
# カーソルを閉じる
cur.close()
# 接続を閉じる
con.close()

# E007, 350000