numbers = [-2, 1, -3, 4, 5, -1, 2]

current = numbers[0]
maximum = numbers[0]

for number in numbers[1:]:
    current = max(number, current + number)
    maximum = max(maximum, current)

print("Maximum subarray sum:", maximum)