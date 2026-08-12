password = input("Enter password: ")

has_digit = False

for character in password:
    if character.isdigit():
        has_digit = True
        break

if has_digit:
    print("Password contains a digit")
else:
    print("Password must contain at least one digit")