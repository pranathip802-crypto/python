numbers = [10, 20, 10, 30, 20, 10]

most_frequent = numbers[0]

for number in numbers:
    if numbers.count(number) > numbers.count(most_frequent):
        most_frequent = number

print("Most frequent:", most_frequent)