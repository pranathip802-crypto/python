text = input("Enter a string: ")

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        print(ch)