class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


book1 = Book("Python Basics", "John", 500)
book2 = Book("Java Basics", "David", 600)

print(book1.title, book1.author, book1.price)
print(book2.title, book2.author, book2.price)