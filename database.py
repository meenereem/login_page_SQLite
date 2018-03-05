import sqlite3
# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates a file called database.db with a SQLite3 DB
db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db")

cursor = db.cursor()
# cursor.execute('''
#     CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT unique, password TEXT)
# ''')

# email1 = 'blah'
# pass1 = 'blah'
# email2 = 'email@email.email'
# pass2 = 'password'

# cursor.execute('''INSERT INTO users(email, password)
#                   VALUES(?,?)''', (email1, pass1))
# print('First user inserted')
# db.commit()

# cursor.execute('''INSERT INTO users(email, password)
#                   VALUES(?,?)''', (email2, pass2))
# print('Second user inserted')

# db.commit()
db.close()