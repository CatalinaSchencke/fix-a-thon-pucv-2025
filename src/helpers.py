import json
import datetime
from decimal import Decimal

def log_action(action, user_id=None, details=None):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] {action}"
    
    if user_id:
        log_entry += f" - User: {user_id}"
    
    if details:
        log_entry += f" - Details: {details}"
    
    with open('data/transactions.log', 'a') as f:
        f.write(log_entry + '\n')

def format_currency(amount):
    return f"${amount:.2f}"

def sanitize_input(input_str):
    if input_str:
        return input_str.strip().replace('<', '').replace('>', '')
    return ''

def calculate_date_difference(date1, date2):
    d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    return (d2 - d1).days

def get_products_by_category(category):
    with open('data/products.json', 'r') as f:
        products = json.load(f)
    
    return [p for p in products if p.get('category') == category]