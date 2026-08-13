class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages


books = [
    Book("Python", "John", 500, 300),
    Book("Java", "David", 600, 400),
    Book("C++", "Robert", 450, 350)
]

for book in books:
    print(book.title, book.author, book.price, book.pages)