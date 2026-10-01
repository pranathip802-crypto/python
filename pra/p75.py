list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = []

for number in list1:
    if number not in list2:
        result.append(number)

print(result)