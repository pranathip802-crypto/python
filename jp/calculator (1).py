class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


c = Calculator()

print(c.addition(10, 5))
print(c.subtraction(10, 5))
print(c.multiplication(10, 5))
print(c.division(10, 5))