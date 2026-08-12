products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Mobile": 25000,
    "Keyboard": 1500,
    "Monitor": 8000
}

expensive_products = set()

for product, price in products.items():
    if price > 5000:
        expensive_products.add(product)

print("Products above ₹5,000:")
print(expensive_products)