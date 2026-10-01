numbers = [10, 20, 10, 30, 20, 40]

for number in numbers:
    if numbers.count(number) == 1:
        print("First non-repeating:", number)
        break