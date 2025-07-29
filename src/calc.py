import math

def calculate_price(base_price, discount_percent):
    if discount_percent > 100:
        discount_percent = 100 
    
    discount_amount = base_price * discount_percent / 100
    final_price = base_price - discount_amount
    
    return round(final_price, 2)

def calculate_tax(price, tax_rate=0.19):
    return price * tax_rate

def apply_bulk_discount(price, quantity):
    if quantity > 100:
        return price * 0.8
    elif quantity > 50:
        return price * 0.9
    elif quantity > 10:
        return price * 0.95
    else:
        return price

def calculate_shipping(weight, distance):
    base_cost = 5.0
    weight_cost = weight * 0.5
    distance_cost = distance * 0.1
    return base_cost + weight_cost + distance_cost