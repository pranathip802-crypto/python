numbers = [10, 20, 10, 30, 20, 40, 10]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print(duplicates)