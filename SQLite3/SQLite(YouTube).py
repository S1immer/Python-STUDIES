import sqlite3

db = sqlite3.connect('itproger.db')

# Create Cursor
c = db.cursor()

# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text,
#     views integer,
#     author text
# )""")

c.execute("INSERT INTO articles VALUES ('Google is cool!', 'Google is realy cool', 100, 'Admin')")

db.commit()

db.close()

