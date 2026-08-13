class Student:
    # Class variable
    college_name = "ABC College"
    student_count = 0

    # Constructor
    def __init__(self, roll_no, name, age, marks):
        # Instance variables
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

        Student.student_count += 1

    # Instance method
    def display(self):
        print("\nStudent Details")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("College:", Student.college_name)

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    def update(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


students = []


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    student = Student(
        roll_no,
        name,
        age,
        marks
    )

    students.append(student)

    print("Student added successfully")


def display_students():
    if not students:
        print("No students available")
        return

    for student in students:
        student.display()
        print("Grade:", student.grade())


def search_student():
    roll_no = input("Enter Roll No: ")

    for student in students:
        if student.roll_no == roll_no:
            student.display()
            print("Grade:", student.grade())
            return

    print("Student not found")


def update_student():
    roll_no = input("Enter Roll No: ")

    for student in students:
        if student.roll_no == roll_no:
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            marks = float(input("Enter new marks: "))

            student.update(name, age, marks)

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


while True:

    print("\n========== STUDENT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Display Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print(
            "Total objects created:",
            Student.student_count
        )

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice")