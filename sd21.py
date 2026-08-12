numbers = {10, 25, 5, 40, 15}

smallest = None

for number in numbers:
    if smallest is None or number < smallest:
        smallest = number

print("Smallest:", smallest)