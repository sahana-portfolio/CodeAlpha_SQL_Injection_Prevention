import sqlite3

def create_connection():
    conn = sqlite3.connect('secure_users.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(username, encrypted_password):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Basic SQL Injection prevention using parameterized queries (very important)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, encrypted_password))
    
    conn.commit()
    conn.close()

def fetch_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users")
    data = cursor.fetchall()
    conn.close()
    return data
