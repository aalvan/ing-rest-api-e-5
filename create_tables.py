import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS users_app (id INTEGER PRIMARY KEY, name text, permission text, rut INTEGER, campus text, career INTEGER)"
cursor.execute(create_table)

users_app =[ (1, 'Alexis','creator',21567337,'CCC',30),
             (2, 'Catalina','creator',19469646,'CCC',30),
             (3, 'Vicente','creator',19456765,'CCC',72),
             (4, 'Paulo', 'creator',193849581,'CCC',72)
]
insert_query = "INSERT INTO users_app  VALUES (?, ?, ?, ?, ? ,?)"

cursor.executemany(insert_query, users_app)

create_table = "CREATE TABLE IF NOT EXISTS assistants_app (id INTEGER PRIMARY KEY, name text, rut INTEGER, range text, manager INTEGER)"
cursor.execute(create_table)

assistants_app =[ (1,'Alejandro', 21467337,'A',21468337),
             (2,'Camila', 19569646,'B',19569656),
             (3,'Victor', 19756765,'C',19756766)
]
insert_query = "INSERT INTO assistants_app  VALUES (?, ?, ?, ?, ?)"

cursor.executemany(insert_query, assistants_app)

select_query = "SELECT * FROM users_app"

for row in cursor.execute(select_query):
    print(row)

select_query = "SELECT * FROM assistants_app"

for row in cursor.execute(select_query):
    print(row)


connection.commit()

connection.close()