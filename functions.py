import os

FILE_NAME = "students.txt"


def add_student():
    print("\n========== ADD STUDENT ==========")

    # Validate name
    while True:
        name = input("Enter Student Name: ").strip()

        if not name:
            print("❌ Name cannot be empty. Please try again.")
        elif not name.replace(" ", "").isalpha():
            print("❌ Name should contain only letters.")
        else:
            break

    # Validate roll number
    while True:
        roll = input("Enter Roll Number: ").strip()

        if not roll:
            print("❌ Roll number cannot be empty.")
        elif not roll.isdigit():
            print("❌ Roll number must contain only numbers.")
        else:
            break

    # Validate course
    while True:
        course = input("Enter Course: ").strip()

        if not course:
            print("❌ Course cannot be empty.")
        else:
            break

    # Check whether file exists
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    # Check duplicate roll number
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                existing_name, existing_roll, existing_course = line.strip().split(",")

                if existing_roll == roll:
                    print("\n❌ Roll Number already exists!\n")
                    return

    # Save student
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
    search_term = input("Enter Name or Roll Number to Search: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, roll, course = line.strip().split(",")

            if search_term in name.lower() or search_term == roll:
                print("\nStudent Found")
                print(f"Name   : {name}")
                print(f"Roll   : {roll}")
                print(f"Course : {course}")
                print("----------------------------")
                found = True

    if not found:
        print("\n❌ Student Not Found!\n")


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

def update_student():
    roll = input("Enter Roll Number to Update: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

    students = []
    updated = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, r, course = line.strip().split(",")

            if r == roll:
                print("\nCurrent Details")
                print(f"Name   : {name}")
                print(f"Course : {course}")

                new_name = input("Enter New Name: ")
                new_course = input("Enter New Course: ")

                students.append(f"{new_name},{roll},{new_course}\n")
                updated = True

            else:
                students.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(students)

    if updated:
        print("\n✅ Student Updated Successfully!\n")
    else:
        print("\n❌ Student Not Found!\n")

def get_total_students():
    if not os.path.exists(FILE_NAME):
        return 0

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    return len(students)

def show_dashboard():
    total = get_total_students()

    print("\n=========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=========================================")
    print("\n              DASHBOARD")
    print("-----------------------------------------")
    print(f"Total Students : {total}")
    print("-----------------------------------------")