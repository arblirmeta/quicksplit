import sqlite3
import os

# SQLite Tutorial von: https://docs.python.org/3/library/sqlite3.html
# Flask + SQLite von: https://flask.palletsprojects.com/en/2.0.x/patterns/sqlite3/

# Datenbankdatei im gleichen Ordner wie das Script
DATABASE = 'quicksplit.db'

def get_db_connection():
    """Verbindung zur SQLite Datenbank herstellen"""
    conn = sqlite3.connect(DATABASE)
    # row_factory Trick von Flask SQLite Tutorial - macht Ergebnisse einfacher
    conn.row_factory = sqlite3.Row  
    return conn

def init_database():
    """Erstellt alle nötigen Tabellen wenn sie noch nicht existieren"""
    # SQL CREATE TABLE Syntax von w3schools.com/sql/sql_create_table.asp
    conn = get_db_connection()
    
    # Tabelle für Events erstellen
    # FOREIGN KEY Syntax von sqlite.org/foreignkeys.html
    conn.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabelle für User erstellen
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            event_id INTEGER NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')
    
    # Tabelle für Expenses erstellen
    conn.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            date DATE DEFAULT CURRENT_DATE,
            payer_id INTEGER NOT NULL,
            event_id INTEGER NOT NULL,
            FOREIGN KEY (payer_id) REFERENCES users (id),
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')
    
    # Many-to-Many Relationship - von Database Design Tutorial
    # Composite Primary Key von sqlite.org/lang_createtable.html
    conn.execute('''
        CREATE TABLE IF NOT EXISTS expense_participants (
            expense_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            PRIMARY KEY (expense_id, user_id),
            FOREIGN KEY (expense_id) REFERENCES expenses (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Datenbank wurde initialisiert!")

# if __name__ == '__main__' Trick von Python Best Practices
if __name__ == '__main__':
    init_database()
