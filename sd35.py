products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Pen": 50
}

for product, price in products.items():
    if price > 1000:
        print(product, ":", price)