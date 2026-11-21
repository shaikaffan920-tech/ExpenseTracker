import sqlite3
import os

DB_PATH = os.path.join("database","expenses.db")

def connect_db():
    os.makedirs("database",exist_ok= True)
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        transactions_type TEXT NOT NULL,
        date 
        )
    """)
    cursor.execute("PRAGMA table_info(transactions)")
    columns = [row[1] for row in cursor.fetchall()]

    if "transactions_type" in columns:
        cursor.execute("""
        ALTER TABLE transactions
        DROP COLUMN transactions_type
    """)
    print("Old incorrect column removed!")
    print("existing coloumns:",columns)

    cursor.execute("PRAGMA table_info(transactions)")
    columns = [row[1] for row in cursor.fetchall()]

    print("updated columns:",columns)

    conn.commit()
    conn.close()

if __name__=="__main__":
    create_table()
    print("Database Created successfully")