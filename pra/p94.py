numbers = [10, 22, 9, 33, 21, 50]

longest = []

for number in numbers:
    if not longest or number > longest[-1]:
        longest.append(number)

print(longest)