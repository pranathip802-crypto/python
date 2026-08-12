words = {
    "apple": "A fruit",
    "computer": "An electronic device",
    "python": "A programming language",
    "book": "A collection of pages"
}

word = input("Enter a word: ")

if word in words:
    print("Meaning:", words[word])
else:
    print("Word not found")