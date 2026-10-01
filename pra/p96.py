numbers = [1, 2, 3, 2, 1]
target = 5

for i in range(len(numbers)):
    total = 0

    for j in range(i, len(numbers)):
        total = total + numbers[j]

        if total == target:
            print(numbers[i:j + 1])