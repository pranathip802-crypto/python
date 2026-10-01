numbers = [10, 20, 10, 30, 20, 40, 10]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print(result)p72.py
numbers = [10, 20, 10, 30, 20, 40, 10]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print(duplicates)