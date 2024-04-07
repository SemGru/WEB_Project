import sqlite3

DB = sqlite3.connect('test_web_db.db')
SQL = DB.cursor()
SQL.execute("""CREATE TABLE IF NOT EXISTS tasks  (
    tasks_name TEXT)""")
DB.commit()

al = SQL.execute("SELECT * FROM users ORDER BY score DESC").fetchall()


def save_plaer(name, score):
    SQL.execute(f"INSERT INTO users VALUES (?, ?)", (name, score))
    DB.commit()
