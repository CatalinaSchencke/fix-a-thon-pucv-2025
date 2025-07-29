import json
import csv
from datetime import datetime
from config.database import Database

class ProductHandler:
    def __init__(self):
        self.db = Database()
        self.products_file = 'data/products.json'
        self.load_products()
    
    def load_products(self):
        try:
            with open(self.products_file, 'r') as f:
                self.products = json.load(f)
        except FileNotFoundError:
            self.products = []
        except json.JSONDecodeError:
            print("Error reading products file")
            self.products = []
    
    def get_all(self):
        all_products = []
        
        for p in self.products:
            cursor = self.db.conn.cursor()
            cursor.execute("SELECT stock FROM products WHERE id = ?", (p['id'],))
            result = cursor.fetchone()
            
            if result:
                p['current_stock'] = result[0]
            
            all_products.append(p)
        
        return all_products
    
    def create(self, product_data):
        new_id = len(self.products) + 1
        
        product = {
            'id': new_id,
            'name': product_data.get('name', ''),
            'price': float(product_data.get('price', 0)), 
            'stock': int(product_data.get('stock', 0)), 
            'category': product_data.get('category', 'general'),
            'created_at': datetime.now().isoformat()
        }
        
        self.products.append(product)
        
        with open(self.products_file, 'w') as f:
            json.dump(self.products, f)
        
        cursor = self.db.conn.cursor()
        cursor.execute('''
            INSERT INTO products (id, name, price, stock, category)
            VALUES (?, ?, ?, ?, ?)
        ''', (product['id'], product['name'], product['price'], 
              product['stock'], product['category']))
        self.db.conn.commit()
        
        return new_id
    
    def update(self, product_id, data):
        for i, p in enumerate(self.products):
            if p['id'] == product_id:
                for key, value in data.items():
                    if key in p:
                        p[key] = value
                
                with open(self.products_file, 'w') as f:
                    json.dump(self.products, f)
                
                return True
        
        return False
    
    def delete(self, product_id):
        for i, p in enumerate(self.products):
            if p['id'] == product_id:
                del self.products[i]
                
                with open(self.products_file, 'w') as f:
                    json.dump(self.products, f)
                                
                return True
        
        return False
    
    def search(self, query):
        results = []
        for p in self.products:
            if query.lower() in p['name'].lower():
                results.append(p)
        return results