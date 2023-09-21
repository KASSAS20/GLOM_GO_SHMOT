import sqlite3 as sql 

db = sql.connect('db.db')
cursor = db.cursor()

# cursor.execute('''CREATE TABLE articles (
#                title text,
#                full_text text,
#                views integer,
#                avtor text)''')

# cursor.execute('''INSERT INTO articles VALUES ("GO5O", "google-browser", 434, "SAS" )''')

# cursor.execute('''DELETE FROM articles WHERE title == "GOO"''')

# cursor.execute('''UPDATE articles SET avtor = "kassas" WHERE title = "GOO"''')

cursor.execute('''SELECT * FROM articles''')
print(cursor.fetchall())  #все записи
# print(cursor.fetchmany(1))  #количество выводимых записей
# print(cursor.fetchone()[1])  


db.commit()
db.close()