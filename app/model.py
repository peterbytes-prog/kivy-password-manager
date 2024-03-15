import sqlite3

def init_db():
    db_path = 'passwords.db'  # Consider specifying an absolute path for testing

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords(
            id INTEGER PRIMARY KEY,
            title TEXT, username TEXT,
            password TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )''')
    t = conn.commit()


    # Create the users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')

    t = conn.commit()

    conn.close()


# init_db()
