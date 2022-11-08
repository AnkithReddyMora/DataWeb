import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()
try:
     cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Maggie')")
cursor.execute("insert into list (description) values ('chicken')")
cursor.execute("insert into list (description) values('almond joy')")
cursor.execute("insert into list (description) values ('danon')")
cursor.execute("insert into list (description) values ('bread')")
connection.commit()
connection.close()

print("done")