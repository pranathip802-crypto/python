numbers = [1, 2, 3, 5]

n = 5

expected_sum = n * (n + 1) // 2

actual_sum = 0

for number in numbers:
    actual_sum = actual_sum + number

missing = expected_sum - actual_sum

print("Missing number:", missing)p80.py
