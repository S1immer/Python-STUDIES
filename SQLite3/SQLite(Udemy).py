import sqlite3

DB_NAME = "sqlite_db.db"


# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "SELECT * FROM courses WHERE reviews_qty>=30"
#     sql_cursor = sqlite_conn.execute(sql_request)
#     # for record in sql_cursor:
#     #     print(record[1])
#     records = sql_cursor.fetchall()
#     print(records)


# Create new table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
    id integer PRIMARY KEY,
    title text NOT NULL,
    studies_qty integer,
    reviews_qty
    );"""
    sqlite_conn.execute(sql_request)




# # Add records to the courses table
# courses = [
#     (351, "JavaScript course", 415, 100),
#     (614, "C++ course", 161, 10),
#     (721, "Java full course", 100, 35)
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()
