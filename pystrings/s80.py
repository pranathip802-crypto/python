text = input("Enter a string: ")

while True:

    print("\n===== STRING MENU =====")
    print("1. Reverse")
    print("2. Palindrome")
    print("3. Vowel Count")
    print("4. Word Count")
    print("5. Character Frequency")
    print("6. Uppercase")
    print("7. Lowercase")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("Reverse:", text[::-1])

    elif choice == "2":

        if text == text[::-1]:
            print("Palindrome")
        else:
            print("Not a palindrome")

    elif choice == "3":

        count = 0

        for ch in text:
            if ch.lower() in "aeiou":
                count += 1

        print("Vowel count:", count)

    elif choice == "4":

        words = text.split()

        print("Word count:", len(words))

    elif choice == "5":

        frequency = {}

        for ch in text:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        print("Character frequency:", frequency)

    elif choice == "6":

        print("Uppercase:", text.upper())

    elif choice == "7":

        print("Lowercase:", text.lower())

    elif choice == "8":

        print("Program ended.")
        break

    else:

        print("Invalid choice")