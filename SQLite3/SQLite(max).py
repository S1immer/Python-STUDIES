import sqlite3


class Sql:
    def create_table(self):
        conn = sqlite3.connect('dan_db.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tabl(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                    )''')
        conn.commit()
        conn.close()


    def create_name(self, name, age):
        conn = sqlite3.connect('dan_db.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO tabl(name, age) VALUES(?,?)', (name, age))
        conn.commit()
        conn.close()


    def delete_id_for_num(self, id):
        conn = sqlite3.connect('dan_db.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM tabl WHERE id = ?', (id, ))
        conn.commit()
        conn.close()


    # def rename_table(self):
    #     conn = sqlite3.connect('dan_db.db')
    #     cur = conn.cursor()
    #     cur.execute('ALTER TABLE data RENAME TO tabl')
    #     conn.commit()
    #     conn.close()


# Создаем объект класса
clas = Sql()

# Создаем таблицу (раскомментируйте эту строку, если таблица еще не создана)
# clas.create_table()

# Добавляем записи в таблицу
# clas.create_name('Dan', 21)
# clas.create_name('Max', 16)

# Удаляем запись по идентификатору
# clas.delete_id_for_num(3)

# clas.rename_table()
