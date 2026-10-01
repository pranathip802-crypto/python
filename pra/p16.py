numbers = [10, -5, 0, 20, -2, 0]

positive = 0
negative = 0
zero = 0

for number in numbers:

    if number > 0:
        positive = positive + 1

    elif number < 0:
        negative = negative + 1

    else:
        zero = zero + 1

print("Positive =", positive)
print("Negative =", negative)
print("Zero =", zero)