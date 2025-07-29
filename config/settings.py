import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DB_URL', 'sqlite:///default.db')
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', "mi_clave_super_secreta_123")
MAX_PRODUCTS = int(os.getenv('MAX_PRODUCTS', 1000))
MAX_USERS = int(os.getenv('MAX_USERS', 50))

# Variables
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
REDIS_URL = "redis://localhost:6379"

def get_db_connection():
    # Función en archivo de configuración - mal ubicada
    import sqlite3
    return sqlite3.connect('data/shop.db')

DB_HOST = "localhost"
DB_NAME = "shop_db"
DB_USER = "admin"
DB_PASS = "123456"