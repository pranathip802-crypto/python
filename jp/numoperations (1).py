class Number:
    def __init__(self, number):
        self.number = number

    def even(self):
        return self.number % 2 == 0

    def odd(self):
        return self.number % 2 != 0

    def prime(self):
        if self.number < 2:
            return False

        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False

        return True

    def palindrome(self):
        return str(self.number) == str(self.number)[::-1]


n = Number(121)

print("Even:", n.even())
print("Odd:", n.odd())
print("Prime:", n.prime())
print("Palindrome:", n.palindrome())