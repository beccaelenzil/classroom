TYPES = ["drip", "latte", "cappuccino"]
SIZES = ["small", "medium", "large"]
TYPE_PRICES = [1.5, 3.7, 3.2]
SIZE_PRICES = [1, 1.3, 1.6]

def coffee_price(type, size):
    if type == "drip":
        price = 1.5
    elif type == "latte":
        price = 3.7
    elif type == "cappuccino":
        price = 3.2
    # else:
    #     return False

    if size == "small":
       price *= 1
    elif size == "medium":
       price *= 1.3
    elif size == "large":
       price *= 1.6
    # else:
    #     return False

    return f"{price:0.2f}"

price = coffee_price("drip", "medium")
print(price)


def price_by_type(type):
    if type == "drip":
        price = 1.5
    elif type == "latte":
        price = 3.7
    elif type == "cappuccino":
        price = 3.2
    else:
        return False
    
    return price

def price_by_size(size):
    if size == "small":
        multiplier = 1
    elif size == "medium":
        multiplier = 1.3
    elif size == "large":
        multiplier = 1.6
    else:
        return False

    return multiplier


def coffee_price_refactor(type, size):
    
    # if type not in TYPES:
    #     return "Invalid type"

    # if size not in SIZES:
    #     return "Invalid size"
    
    price = price_by_type(type)
    multiplier = price_by_size(size)

    if not price:
        return "Please enter a valid type."
    
    if not multiplier:
        return "Please enter a valid size."

    return f"{price*multiplier:0.2f}"

price = coffee_price_refactor("drip", "medium")
print(price)

def coffee_price_loops(type, size):

    for i in range(len(TYPES)):
        if type == TYPES[i]:
            price = TYPE_PRICES[i]

    for i in range(len(SIZES)):
        if size == SIZES[i]:
            price *= SIZE_PRICES[i]

    return f"{price:0.2f}"

price = coffee_price_loops("drip", "medium")
print(price)          


def price_by_type(type):
    for i in range(len(TYPES)):
        if type == TYPES[i]:
            price = TYPE_PRICES[i]
    
    return price

def price_by_size(size):
    for i in range(len(SIZES)):
        if size == SIZES[i]:
            multiplier = SIZE_PRICES[i]

    return multiplier



# def coffee_price_refactor(type, size):

#     if type not in TYPES:
#         return "Invalid type"

#     if size not in SIZES:
#         return "Invalid size"
    
#     price = price_by_type(type)
#     price *= price_by_size(size)

#     return f"{price:0.2f}"





