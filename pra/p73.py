numbers = [10, 20, 10, 30, 20, 40]

unique = []

for number in numbers:
    if numbers.count(number) == 1:
        unique.append(number)

print(unique)