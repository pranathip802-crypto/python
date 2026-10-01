numbers = [-2, 1, -3, 4, 5, -1, 2]

current = numbers[0]
maximum = numbers[0]

start = 0
best_start = 0
best_end = 0

for i in range(1, len(numbers)):
    if numbers[i] > current + numbers[i]:
        current = numbers[i]
        start = i
    else:
        current = current + numbers[i]

    if current > maximum:
        maximum = current
        best_start = start
        best_end = i

result = numbers[best_start:best_end + 1]

print("Subarray:", result)
print("Sum:", maximum)