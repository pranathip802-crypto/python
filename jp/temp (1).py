class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


temp = Temperature()

print(temp.celsius_to_fahrenheit(25))
print(temp.fahrenheit_to_celsius(77))