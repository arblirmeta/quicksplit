import sqlite3
import os

# Datenbankdatei im gleichen Ordner wie das Script
DATABASE = 'quicksplit.db'

def get_db_connection():
    """Verbindung zur SQLite Datenbank herstellen"""
    # Stellt eine Verbindung zur Datenbank her
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Das macht es einfacher mit den Daten zu arbeiten
    return conn

def init_database():
    """Erstellt alle nötigen Tabellen wenn sie noch nicht existieren"""
    conn = get_db_connection()
    
    # Tabelle für Events erstellen
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
    
    # Tabelle für ExpenseParticipants erstellen (wer war bei welcher Ausgabe dabei)
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

# Wenn das Script direkt ausgeführt wird, Datenbank initialisieren
if __name__ == '__main__':
    init_database()
