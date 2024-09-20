import sqlite3


DB_NAME = "simple_database.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOTE EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER
);
"""

cursor.execute(create_table_query)

conn.commit()
conn.close()

print("Table 'users' created.")


