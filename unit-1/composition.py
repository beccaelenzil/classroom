class Product:
 
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_cost(self):
        return self.price * self.quantity

class ShippingAddress:

    def __init__(self, name, street_address, city, state, zip):
        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip

class ShoppingCart:

    def __init__(self, products, shipping_address):
        self.products = products
        self.shipping_address = shipping_address

    def calculate_total_cost(self):
        total_price = 0.0

        for product in self.products:
            #----Refer to this line for Check for Understanding Question 2----
            total_price += product.calculate_cost()

        return total_price

    def summary(self):
        print(len(self.products),"products will be shipped to", self.shipping_address.name,".")

p1 = Product(5.00, 5)
p2 = Product(2.50, 13)
p3 = Product(77.99, 2)
products = [p1, p2, p3]

ravis_address = ShippingAddress(
    name="Ravi", 
    street_address="123 John St", 
    city="Seattle",
    state="WA",
    zip="98112"
    )

sc = ShoppingCart(products, ravis_address)

total_cost = sc.calculate_total_cost()

print(f"The total cost of the products in the shopping cart is ${total_cost}")
sc.summary()