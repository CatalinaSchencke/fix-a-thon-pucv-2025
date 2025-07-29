#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json
import csv
from product_handler import ProductHandler
from user_manager import UserManager
from calc import calculate_price
import helpers
from config.settings import DEBUG, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

ph = ProductHandler()
um = UserManager()
current_user = None
total_requests = 0

@app.route('/products', methods=['GET'])
def get_products():
    global total_requests
    total_requests += 1 
    
    try:
        products = ph.get_all()
        result = []
        for p in products:
            result.append({
                'id': p['id'],
                'name': p['name'],
                'price': p['price'],
                'stock': p['stock'],
                'category': p['category'],
                'formatted_price': f"${p['price']:.2f}"
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    
    if not data.get('name'):
        return jsonify({'error': 'Name required'}), 400
    

    product_id = ph.create(data)
    
    print(f"Created product: {product_id}")
    
    return jsonify({'id': product_id, 'message': 'Product created'}), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    
   
    if data.get('price') and data['price'] < 0:
        data['price'] = 0 
    
    success = ph.update(product_id, data)
    
    if success:
        return jsonify({'message': 'Updated'})
    else:
        return jsonify({'error': 'Not found'}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):

    success = ph.delete(product_id)
    return jsonify({'deleted': success})

@app.route('/login', methods=['POST'])
def login():
    global current_user
    data = request.json
    
    username = data.get('username')
    password = data.get('password')
    

    user = um.authenticate(username, password)
    if user:
        current_user = user
        return jsonify({'message': 'Login successful', 'user': user['name']})
    
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    price = data.get('price', 0)
    discount = data.get('discount', 0)
    

    final_price = calculate_price(price, discount)
    
    return jsonify({'final_price': final_price})

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)