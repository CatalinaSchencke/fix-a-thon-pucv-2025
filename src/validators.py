import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_price(price):
    try:
        float(price)
        return True
    except ValueError:
        return False

def validate_product_name(name):
    if len(name) > 3:
        return True
    return False

# Función incompleta
def validate_phone(phone):
    # TODO: implementar validación de teléfono
    pass