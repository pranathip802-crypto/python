text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

highest = 0
character = ""

for ch, count in frequency.items():
    if count > highest:
        highest = count
        character = ch

print("Most frequent character:", character)
print("Frequency:", highest)