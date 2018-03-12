import sqlite3
db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db",  check_same_thread=False)
# cursor = db.cursor()
# cursor.execute('''
#     CREATE TABLE user_sessions(id INTEGER PRIMARY KEY, email TEXT unique, token TEXT unique)
# ''')
# cursor.execute('''
#     CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT unique, password TEXT)
# ''')
# db.commit()
# db.close()