# sqlite3モジュールをインポートする
import sqlite3

# 妻女するレコードの社員IDをキー入力する
emp_id = input("削除する社員ID-->")

# データベースに接続してコネクションオブジェクトを取得する
con = sqlite3.connect("sample.db")
# カーソルオブジェクトを取得する
cur = con.cursor()
# SQL文を完成させて実行する
cur.execute("DELETE FROM Employee WHERE emp_id = ?", (emp_id,))

# 削除をコミットする
con.commit()
# カーソルを閉じる
cur.close()
# 接続を閉じる
con.close()

# E007