import os

FILE_NAME = "students.txt"


def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{course}\n")

    print("\nStudent Added Successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("\nNo Student Records Found!\n")
        return

    print("\n------ Student Records ------")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, roll, course = line.strip().split(",")
            print(f"Name   : {name}")
            print(f"Roll   : {roll}")
            print(f"Course : {course}")
            print("----------------------------")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo Records Found!\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, r, course = line.strip().split(",")

            if r == roll:
                print("\nStudent Found")
                print(f"Name   : {name}")
                print(f"Roll   : {r}")
                print(f"Course : {course}")
                found = True
                break

    if not found:
        print("\nStudent Not Found!\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo Records Found!\n")
        return

    students = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, r, course = line.strip().split(",")

            if r != roll:
                students.append(line)
            else:
                deleted = True

    with open(FILE_NAME, "w") as file:
        file.writelines(students)

    if deleted:
        print("\nStudent Deleted Successfully!\n")
    else:
        print("\nStudent Not Found!\n")


while True:

    print("\n===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Try Again.\n")