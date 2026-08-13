class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display(self):
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Date:", self.date)


patients = []
doctors = []
appointments = []


def add_patient():
    pid = input("Patient ID: ")
    name = input("Patient Name: ")
    age = int(input("Age: "))

    patients.append(Patient(pid, name, age))


def add_doctor():
    did = input("Doctor ID: ")
    name = input("Doctor Name: ")
    specialization = input("Specialization: ")

    doctors.append(
        Doctor(did, name, specialization)
    )


def create_appointment():
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = input("Appointment Date: ")

    patient = None
    doctor = None

    for p in patients:
        if p.patient_id == pid:
            patient = p

    for d in doctors:
        if d.doctor_id == did:
            doctor = d

    if patient and doctor:
        appointments.append(
            Appointment(patient, doctor, date)
        )
        print("Appointment created")
    else:
        print("Patient or doctor not found")


def display_appointments():
    for appointment in appointments:
        appointment.display()


while True:
    print("\n1. Add Patient")
    print("2. Add Doctor")
    print("3. Create Appointment")
    print("4. Display Appointments")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        create_appointment()
    elif choice == "4":
        display_appointments()
    elif choice == "5":
        break
    else:
        print("Invalid choice")