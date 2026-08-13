class Room:
    def __init__(self, room_no, price):
        self.room_no = room_no
        self.price = price
        self.available = True


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Booking:
    def __init__(self, customer, room, days):
        self.customer = customer
        self.room = room
        self.days = days

        room.available = False

    def bill(self):
        return self.room.price * self.days

    def display(self):
        print("Customer:", self.customer.name)
        print("Room:", self.room.room_no)
        print("Days:", self.days)
        print("Bill:", self.bill())


rooms = [
    Room(101, 1500),
    Room(102, 2000),
    Room(103, 2500)
]

bookings = []


def display_rooms():
    for room in rooms:
        status = "Available" if room.available else "Booked"
        print(room.room_no, room.price, status)


def book_room():
    name = input("Customer Name: ")
    phone = input("Phone: ")
    room_no = int(input("Room Number: "))
    days = int(input("Number of days: "))

    selected_room = None

    for room in rooms:
        if room.room_no == room_no:
            selected_room = room

    if selected_room is None:
        print("Room not found")
        return

    if not selected_room.available:
        print("Room already booked")
        return

    customer = Customer(name, phone)

    booking = Booking(
        customer,
        selected_room,
        days
    )

    bookings.append(booking)

    print("Room booked successfully")


def display_bookings():
    for booking in bookings:
        booking.display()


while True:
    print("\n1. Display Rooms")
    print("2. Book Room")
    print("3. Display Bookings")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        display_bookings()
    elif choice == "4":
        break
    else:
        print("Invalid choice")