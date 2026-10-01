list1 = [10, 20, 30, 40]
list2 = [20, 30, 40, 50]
list3 = [30, 40, 60]

result = []

for number in list1:
    if number in list2 and number in list3:
        result.append(number)

print(result)