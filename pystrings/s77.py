username = input("Enter username: ")

if username == "":
    print("Username cannot be empty")

elif len(username) < 5:
    print("Username must contain at least 5 characters")

elif not username.isalnum():
    print("Username should contain only letters and numbers")

else:
    print("Valid Username")