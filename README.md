# Smart Campus & Student Management System

A comprehensive Python-based desktop console application developed as the Week 6 Final Project for the InternNova Python Internship.

## Project Description
The **Smart Campus & Student Management System** enables automated management of student academic profiles, registrations, search queries, and secure records storage. It is architected using Python's Object-Oriented Programming (OOP) paradigm, standard file handling routines, robust exception catching, and modular system design.

## Features
- **Student Profile Management:** Add, view, search, and manage student academic details.
- **Persistent File Storage:** Reads from and writes updates to `database.txt` automatically.
- **Data Validation & Error Handling:** Prevents crashes using `try`/`except` blocks for all user inputs and file I/O operations.
- **Role-Based Polymorphism:** Uniformly renders dashboards for both students and faculty administrators.
- **Encapsulated Security:** Protects sensitive user data via private attributes with verification methods.
- **Automated Metadata:** Uses Python's standard libraries to log timestamps and generate reference IDs.

## Technologies Used
- **Language:** Python 3.x
- **Development Environment:** Visual Studio Code
- **Version Control:** Git & GitHub

## Python Concepts Implemented
- **Python Fundamentals:** Variables, data types, arithmetic/logical operators, input/output formatting.
- **Control Flow:** `while` loops for continuous menu navigation and `if-elif-else` conditional logic.
- **Data Structures:** Lists of custom objects, dictionaries, and string manipulation.
- **File Handling:** Creation, reading, appending, and writing persistent file storage (`database.txt`).
- **Exception Handling:** Robust input validation (`ValueError`, `IOError`, `FileNotFoundError`).
- **Python Standard Libraries:** `datetime` for timestamps, `random` for reference ID generation, `os` for path verification.
- **Object-Oriented Programming (OOP):**
  - **Classes & Objects:** Real-world entities representing students and faculty.
  - **Constructors:** Parameterized `__init__` for clean state initialization.
  - **Inheritance:** `Student` and `FacultyAdmin` inheriting from abstract base class `User`.
  - **Polymorphism:** Shared `.get_dashboard()` method with distinct class behaviors.
  - **Encapsulation:** Private attribute `__security_pin` managed with getter/setter methods.
  - **Abstraction:** Interface contract enforced via `abc.ABC` and `@abstractmethod`.

## Installation & Setup
1. Clone the repository to your local system:
   ```bash
   git clone [https://github.com/](https://github.com/)<YOUR_GITHUB_USERNAME>/Python_Week_6_Final_Project.git