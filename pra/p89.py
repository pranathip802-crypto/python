numbers = [0, 10, 0, 20, 30, 0, 40]

result = []

for number in numbers:
    if number != 0:
        result.append(number)

for number in numbers:
    if number == 0:
        result.append(number)

print(result)