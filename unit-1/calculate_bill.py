def calculate_bill(items):
    subtotal = 0
    sales_tax = 0.8
    tip = 0.2

    for i in range(1, len(items)):
        subtotal += items[i]["price"]

    total = subtotal * sales_tax * tip

    return total

items = [ {
    "name": "Pasta",
    "price": 14.99,
    },
    {
    "name": "Dumplings",
    "price": 9.99,
    },
    {
    "name": "Diet Coke",
    "price": 2.99,
    },
    {
    "name": "Ice T",
    "price": 0.89,
    },
    {
    "name": "Green Curry Chicken",
    "price": 18.39,
    },
]

bill = calculate_bill(items)
print(f"{bill=}")