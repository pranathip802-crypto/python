class BankAccount:
    def __init__(self, account_no, holder, balance=0):
        self.account_no = account_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def display(self):
        print("Account No:", self.account_no)
        print("Holder:", self.holder)
        print("Balance:", self.balance)


accounts = []


def create_account():
    account_no = input("Enter Account Number: ")
    holder = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    accounts.append(
        BankAccount(account_no, holder, balance)
    )

    print("Account created successfully")


def find_account(account_no):
    for account in accounts:
        if account.account_no == account_no:
            return account

    return None


while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        account_no = input("Enter Account Number: ")
        account = find_account(account_no)

        if account:
            amount = float(input("Enter amount: "))
            account.deposit(amount)
        else:
            print("Account not found")

    elif choice == "3":
        account_no = input("Enter Account Number: ")
        account = find_account(account_no)

        if account:
            amount = float(input("Enter amount: "))
            account.withdraw(amount)
        else:
            print("Account not found")

    elif choice == "4":
        account_no = input("Enter Account Number: ")
        account = find_account(account_no)

        if account:
            print("Balance:", account.balance)
        else:
            print("Account not found")

    elif choice == "5":
        account_no = input("Enter Account Number: ")
        account = find_account(account_no)

        if account:
            account.display()
        else:
            print("Account not found")

    elif choice == "6":
        break

    else:
        print("Invalid choice")