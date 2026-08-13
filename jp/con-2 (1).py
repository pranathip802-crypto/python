class Calculator:
    def add(self, a, b):
        return a + b

    def calculate(self, a, b):
        result = self.add(a, b)
        return result * 2


calc = Calculator()

print(calc.calculate(10, 20))