# Week 6: Final Python Project - Smart Campus & Student Management System
# Developed by: Debojyoti Ghosh
# Enrollment: 12024054006216 | Roll: 214 | Semester: 5th Sem
# Institute of Engineering and Management (IEM), Kolkata | Behala 700061

import os
import datetime
import random
from abc import ABC, abstractmethod

DB_FILE = "database.txt"

# =====================================================================
# 1. ABSTRACTION & ENCAPSULATION (OOP)
# =====================================================================
class User(ABC):
    """Abstract Base Class representing a system user."""
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        # Private attribute demonstrating Encapsulation
        self.__security_pin = "1234"

    # Encapsulation: Getter and Setter for private PIN
    def verify_pin(self, pin_input):
        return self.__security_pin == pin_input

    def update_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__security_pin = new_pin
            return True
        return False

    @abstractmethod
    def get_dashboard(self):
        """Polymorphic abstract method implemented by subclasses."""
        pass


# =====================================================================
# 2. INHERITANCE & POLYMORPHISM (OOP)
# =====================================================================
class Student(User):
    """Derived Child Class representing a student."""
    def __init__(self, user_id, name, email, roll_no, department, semester, cgpa):
        super().__init__(user_id, name, email)
        self.roll_no = roll_no
        self.department = department
        self.semester = semester
        self.cgpa = cgpa

    # Polymorphic implementation of abstract method
    def get_dashboard(self):
        return (
            f"\n[Student Profile]\n"
            f"ID         : {self.user_id}\n"
            f"Name       : {self.name} (Roll: {self.roll_no})\n"
            f"Department : {self.department} | Semester: {self.semester}\n"
            f"CGPA       : {self.cgpa:.2f}\n"
            f"Email      : {self.email}"
        )


class FacultyAdmin(User):
    """Derived Child Class representing an administrator/mentor."""
    def __init__(self, user_id, name, email, designation):
        super().__init__(user_id, name, email)
        self.designation = designation

    # Polymorphic implementation of abstract method
    def get_dashboard(self):
        return (
            f"\n[Administrator Profile]\n"
            f"Admin ID    : {self.user_id}\n"
            f"Name        : {self.name}\n"
            f"Designation : {self.designation}\n"
            f"Email       : {self.email}"
        )


# =====================================================================
# 3. CORE SYSTEM CLASS: DATA STRUCTURES, FILE HANDLING, EXCEPTION HANDLING
# =====================================================================
class CampusManagementSystem:
    def __init__(self):
        # In-memory List of Student Objects
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        """Loads records from persistent text storage with exception handling."""
        if not os.path.exists(DB_FILE):
            # Seed default profile for Debojyoti Ghosh
            default_student = Student(
                user_id="12024054006216",
                name="Debojyoti Ghosh",
                email="debojyoti.ghosh@iemcal.edu",
                roll_no=214,
                department="BCA",
                semester="5th Semester",
                cgpa=9.25
            )
            self.students.append(default_student)
            self.save_to_file()
            return

        try:
            with open(DB_FILE, "r") as file:
                self.students = []
                for line in file:
                    data = line.strip().split("|")
                    if len(data) == 7:
                        uid, name, email, roll, dept, sem, cgpa = data
                        student = Student(uid, name, email, int(roll), dept, sem, float(cgpa))
                        self.students.append(student)
        except Exception as e:
            print(f"Notice: Error reading database file ({e}). Initializing empty list.")

    def save_to_file(self):
        """Writes all student records to file storage."""
        try:
            with open(DB_FILE, "w") as file:
                for s in self.students:
                    file.write(f"{s.user_id}|{s.name}|{s.email}|{s.roll_no}|{s.department}|{s.semester}|{s.cgpa}\n")
            return True
        except IOError as e:
            print(f"Error saving to disk: {e}")
            return False

    def add_student(self):
        print("\n--- Register New Student ---")
        user_id = input("Enter Enrollment / Registration ID: ").strip()
        name = input("Enter Full Name: ").strip()
        email = input("Enter Email Address: ").strip()

        # Exception Handling for Roll Number
        while True:
            try:
                roll_no = int(input("Enter Roll Number: ").strip())
                break
            except ValueError:
                print("Invalid input! Roll Number must be an integer.")

        department = input("Enter Department (e.g. BCA, CSE): ").strip()
        semester = input("Enter Semester (e.g. 5th Semester): ").strip()

        # Exception Handling for CGPA
        while True:
            try:
                cgpa = float(input("Enter CGPA (0.0 to 10.0): ").strip())
                if 0.0 <= cgpa <= 10.0:
                    break
                else:
                    print("CGPA must be between 0.0 and 10.0.")
            except ValueError:
                print("Invalid input! CGPA must be a numeric value.")

        new_student = Student(user_id, name, email, roll_no, department, semester, cgpa)
        self.students.append(new_student)
        self.save_to_file()

        # Library demonstration: random transaction token & datetime timestamp
        txn_id = random.randint(100000, 999999)
        reg_time = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        print(f"\n[Success] Student '{name}' enrolled successfully!")
        print(f"Registration Ref : #{txn_id} | Timestamp: {reg_time}")

    def view_all_students(self):
        print("\n================ ALL ENROLLED STUDENTS ================")
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            # Demonstrating Polymorphism via get_dashboard()
            print(student.get_dashboard())
            print("-" * 50)

    def search_student(self):
        print("\n--- Search Student Record ---")
        search_query = input("Enter Roll Number or Enrollment ID: ").strip()
        found = False

        for s in self.students:
            if str(s.roll_no) == search_query or s.user_id == search_query:
                print("\n[Record Match Found]")
                print(s.get_dashboard())
                found = True
                break

        if not found:
            print(f"No student record found matching '{search_query}'.")

    def test_polymorphism(self):
        """Explicit demonstration of Polymorphism with User subclasses."""
        print("\n=== Demonstrating OOP Polymorphism ===")
        user_list = [
            Student("12024054006216", "Debojyoti Ghosh", "debojyoti@iemcal.edu", 214, "BCA", "5th Sem", 9.25),
            FacultyAdmin("ADM-101", "Dr. S. K. Mukherjee", "admin@iemcal.edu", "Head of Department")
        ]
        for u in user_list:
            print(u.get_dashboard())
            print("-" * 45)


# =====================================================================
# 4. MAIN MENU DRIVER LOOP
# =====================================================================
def main():
    system = CampusManagementSystem()

    while True:
        print("\n" + "=" * 52)
        print("  SMART CAMPUS & STUDENT MANAGEMENT SYSTEM (IEM)")
        print("=" * 52)
        print("1. View All Students (List & File Read)")
        print("2. Register New Student (Input & File Write)")
        print("3. Search Student by Roll / ID")
        print("4. Demonstrate OOP Polymorphism & Abstraction")
        print("5. Test Encapsulation (PIN Verification)")
        print("6. Exit System")
        print("=" * 52)

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            system.view_all_students()
        elif choice == "2":
            system.add_student()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.test_polymorphism()
        elif choice == "5":
            if system.students:
                test_student = system.students[0]
                pin = input("Enter Security PIN to verify access (Default: 1234): ").strip()
                if test_student.verify_pin(pin):
                    print("PIN Verified: Encapsulated access granted.")
                else:
                    print("Access Denied: Invalid PIN.")
            else:
                print("No student record available to test.")
        elif choice == "6":
            print("\nExiting Campus Management System. Thank you!")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()