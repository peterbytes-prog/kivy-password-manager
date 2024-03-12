import sqlite3

def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY, title TEXT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# init_db()
