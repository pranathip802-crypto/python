numbers = [25, 10, 45, 30, 60]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)