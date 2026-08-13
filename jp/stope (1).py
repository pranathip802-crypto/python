class StringOperations:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

    def count_vowels(self):
        count = 0

        for char in self.text.lower():
            if char in "aeiou":
                count += 1

        return count

    def palindrome(self):
        return self.text == self.text[::-1]


s = StringOperations("madam")

print("Reverse:", s.reverse())
print("Vowels:", s.count_vowels())
print("Palindrome:", s.palindrome())