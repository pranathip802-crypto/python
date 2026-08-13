class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(
            self.roll_no,
            self.name,
            self.age,
            self.course
        )


students = []


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = Student(roll_no, name, age, course)
    students.append(student)

    print("Student added successfully")


def search_student():
    roll_no = input("Enter Roll No: ")

    for student in students:
        if student.roll_no == roll_no:
            student.display()
            return

    print("Student not found")


def update_student():
    roll_no = input("Enter Roll No: ")

    for student in students:
        if student.roll_no == roll_no:
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.course = input("Enter new course: ")

            print("Student updated")
            return

    print("Student not found")


def delete_student():
    roll_no = input("Enter Roll No: ")

    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print("Student deleted")
            return

    print("Student not found")


def display_students():
    if not students:
        print("No students found")
        return

    for student in students:
        student.display()


while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_students()
    elif choice == "6":
        break
    else:
        print("Invalid choice")