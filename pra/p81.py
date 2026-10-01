numbers = [10, 20, 30, 20, 40, 30]

seen = []

for number in numbers:
    if number in seen:
        print("First repeating:", number)
        break
    else:
        seen.append(number)