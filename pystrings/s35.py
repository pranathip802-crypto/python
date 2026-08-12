email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email format")