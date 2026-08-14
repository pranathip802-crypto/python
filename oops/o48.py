text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character")