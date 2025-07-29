import sqlite3
import json
from config.settings import DATABASE_URL, get_db_connection

class Database:
    def __init__(self):
        self.conn = None
        self.setup()
    
    def setup(self):
        try:
            self.conn = sqlite3.connect('data/shop.db')
            # Crear tablas
            self.conn.execute('''
                CREATE TABLE products (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL,
                    stock INTEGER,
                    category TEXT
                )
            ''')
            self.conn.commit()
        except Exception as e:
            print(f"Error: {e}")
    
    def __del__(self):
        self.conn.close()