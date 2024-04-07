import sqlite3
import random
DB = sqlite3.connect('test_web.db')
SQL = DB.cursor()
SQL.execute("""CREATE TABLE IF NOT EXISTS task  (
    number INTEGER,
    task_name TEXT)""")
DB.commit()
count = 1
al = SQL.execute(f"SELECT * FROM task WHERE number == {count}").fetchall()
print(random.choice(al[1]))

def save_plaer(number, task_name):
    SQL.execute(f"INSERT INTO task VALUES (?, ?)", (number, task_name))
    DB.commit()

# import sqlite3
#
# DB = sqlite3.connect('test_web_db.db')
# SQL = DB.cursor()
# SQL.execute("""CREATE TABLE IF NOT EXISTS tasks  (
#     tasks_name TEXT)""")
# DB.commit()
#
# al = SQL.execute("SELECT * FROM tasks").fetchall()
#
# SQL.execute(f"INSERT INTO tasks VALUES (?)", '/static/img/1267.gif')
# # def save_plaer(score):
# #     SQL.execute(f"INSERT INTO tasks VALUES (?)", score)
# #     DB.commit()
# #
# #
# # save_plaer('/static/img/1267.gif')
# # save_plaer('/static/img/1280.gif')
