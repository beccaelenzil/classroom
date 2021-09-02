TYPES = ["drip", "latte", "cappuccino"]
SIZES = ["small", "medium", "large"]
TYPE_PRICES = [1.5, 3.7, 3.2]
SIZE_PRICES = [1, 1.3, 1.6]

def price_by_type(type):
    if type not in TYPES:
        return False
    elif type == "drip":
        price = 1.5
    elif type == "latte":
        price = 3.7
    elif type == "cappuccino":
        price = 3.2
    
    return price

def price_by_size(size):
    if size not in SIZES:
        return False
    elif size == "small":
        multiplier = 1
    elif size == "medium":
        multiplier = 1.3
    elif size == "large":
        multiplier = 1.6

    return multiplier

def coffee_price(type, size):

    if not price_by_type(type):
        return "Invalid type"

    if not price_by_size(size):
        return "Invalid size"
    
    price = price_by_type(type)
    price *= price_by_size(size)

    return f'{price:0.2f}'



def coffee_price(type, size):
    if type not in TYPES:
        return False
    elif type == "drip":
        price = 1.5
    elif type == "latte":
        price = 3.7
    elif type == "cappuccino":
        price = 3.2

    if size not in SIZES:
        return False
    elif size == "small":
        multiplier = 1
    elif size == "medium":
        multiplier = 1.3
    elif size == "large":
        multiplier = 1.6

price = coffee_price("drip", "medium")
print(price)

