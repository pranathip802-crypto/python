numbers = [10, 20, 10, 30, 20, 10]

least_frequent = numbers[0]

for number in numbers:
    if numbers.count(number) < numbers.count(least_frequent):
        least_frequent = number

print("Least frequent:", least_frequent)