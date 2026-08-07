import os

FILE_NAME = "students.txt"


def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    # Check if roll number already exists
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) >= 2 and data[1] == roll:
                    print("\n❌ Roll Number already exists!\n")
                    return

    # Save new student
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{course}\n")

    print("\n✅ Student Added Successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("\nNo Student Records Found!\n")
        return

    print("\n" + "=" * 65)
    print(f"{'Roll No':<12}{'Name':<25}{'Course':<25}")
    print("=" * 65)

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, roll, course = line.strip().split(",")
            print(f"{roll:<12}{name:<25}{course:<25}")

    print("=" * 65)


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