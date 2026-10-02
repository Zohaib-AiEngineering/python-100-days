products = [
    {"name": "Laptop", "price": 999},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 49}
]
for product in products: 
    if product ["price"] < 50: 
        print(product["name"])