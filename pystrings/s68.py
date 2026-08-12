text = input("Enter a string: ")

unique = ""

for ch in text:
    if text.count(ch) == 1:
        unique += ch

print("Unique characters:", unique)