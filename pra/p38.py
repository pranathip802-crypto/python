numbers = [10, 20, 10, 30, 10]

new_list = []

for number in numbers:
    new_list.append(number)

    if number == 10:
        new_list.append(99)

print(new_list)