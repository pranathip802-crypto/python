list1 = [10, 20, 30]
list2 = [30, 40, 50]

result = []

for number in list1 + list2:
    if number not in result:
        result.append(number)

print(result)