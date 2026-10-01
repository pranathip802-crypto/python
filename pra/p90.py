numbers = [10, -5, 20, -10, 30, -2]

result = []

for number in numbers:
    if number < 0:
        result.append(number)

for number in numbers:
    if number >= 0:
        result.append(number)

print(result)