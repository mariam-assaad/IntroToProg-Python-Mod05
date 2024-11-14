# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Mariam Assaad,11/13/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU: str = '''---- Course Registration Program ----
Select from the following menu:  
  1. Register a Student for a Course
  2. Show current data  
  3. Save data to a file
  4. Exit the program
----------------------------------------- '''

FILE_NAME: str = "Enrollments.json"

# Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
json_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Load existing data from the JSON file
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)  # Load data directly as a list of dictionaries
except FileNotFoundError:
    print("The file was not found, starting with an empty student list.")
    students = []
except json.JSONDecodeError:
    print("Error decoding JSON, starting with an empty student list.")
    students = []
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    students = []

while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Option 1: Register a Student
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name should only contain letters.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name should only contain letters.")

            course_name = input("Enter the course name: ")

            # Add student data as a dictionary to the list
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"Registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Option 2: Show Current Data
    elif menu_choice == "2":
        if students:
            print("-" * 50)
            for student in students:
                print(f"Student: {student['FirstName']} {student['LastName']}, Course: {student['CourseName']}")
            print("-" * 50)
        else:
            print("No students registered yet.")


    # Option 3: Save Data to a File
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=4)  # Added indent for readability
            print("Data successfully saved to file.")

            # Display the data that was saved
            print("The following data was saved to the file:")
            for student in students:
                print(f"Student: {student['FirstName']} {student['LastName']}, Course: {student['CourseName']}")

        except IOError:
            print("An error occurred while writing to the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    # Option 4: Exit Program
    elif menu_choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")

print("Program Ended")
