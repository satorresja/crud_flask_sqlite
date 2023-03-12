import sqlite3 as sql

connection = sql.connect("ToDo_data_base.db")

cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS ToDo_data_base""")

sql = """CREATE TABLE ToDo_data_base (
    "id" INTEGER PRIMARY KEY,
    "task" TEXT,
    "completed" BOOLEAN
)"""

cursor.execute(sql)
connection.commit()
connection.close()
