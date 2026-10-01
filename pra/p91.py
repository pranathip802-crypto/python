numbers = [1, 2, 3, 4, 5, 6]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)

for number in numbers:
    if number % 2 != 0:
        result.append(number)

print(result)