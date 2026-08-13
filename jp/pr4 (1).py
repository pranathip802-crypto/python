class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        status = "Issued" if self.issued else "Available"

        print(
            self.book_id,
            self.title,
            self.author,
            status
        )


books = []


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    books.append(Book(book_id, title, author))

    print("Book added")


def search_book():
    title = input("Enter title to search: ")

    for book in books:
        if book.title.lower() == title.lower():
            book.display()
            return

    print("Book not found")


def issue_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book.book_id == book_id:

            if book.issued:
                print("Book already issued")
            else:
                book.issued = True
                print("Book issued")

            return

    print("Book not found")


def return_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book.book_id == book_id:

            if book.issued:
                book.issued = False
                print("Book returned")
            else:
                print("Book was not issued")

            return

    print("Book not found")


def display_books():
    for book in books:
        book.display()


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice")