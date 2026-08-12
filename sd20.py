numbers = {10, 25, 5, 40, 15}

largest = None

for number in numbers:
    if largest is None or number > largest:
        largest = number

print("Largest:", largest)