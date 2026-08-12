text = input("Enter a string: ")

for ch in text:
    if ch.lower() in "aeiou":
        print(ch)