import os
import csv

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
     print("\nStudent Found:")
     print(f"Name   : {name}")
     print(f"Roll   : {r}")
     print(f"Course : {course}")

     confirm = input("\nAre you sure you want to delete? (y/n): ").lower()

     if confirm == "y":
        deleted = True
     else:
        students.append(line)
        print("\nDeletion Cancelled!\n")

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

def sort_students():
    if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

    students = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                name, roll, course = line.strip().split(",")
                students.append([name, roll, course])

    if not students:
        print("\nNo Student Records Found!\n")
        return

    print("\nSort Students By")
    print("1. Name")
    print("2. Roll Number")

    choice = input("Enter your choice: ")

    if choice == "1":
        students = sorted(students, key=lambda student: student[0].lower())

    elif choice == "2":
        students = sorted(students, key=lambda student: int(student[1]))

    else:
        print("\n❌ Invalid choice!\n")
        return

    print("\n" + "=" * 65)
    print(f"{'Roll No':<12}{'Name':<25}{'Course':<25}")
    print("=" * 65)

    for student in students:
        print(f"{student[1]:<12}{student[0]:<25}{student[2]:<25}")

    print("=" * 65)

def filter_by_course():
    if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

    selected_course = input("Enter Course to Filter: ").strip().lower()

    found = False

    print("\n" + "=" * 65)
    print(f"{'Roll No':<12}{'Name':<25}{'Course':<25}")
    print("=" * 65)

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                name, roll, course = line.strip().split(",")

                if course.strip().lower() == selected_course:
                    print(f"{roll:<12}{name:<25}{course:<25}")
                    found = True

    print("=" * 65)

    if not found:
        print("\n❌ No students found for this course.\n")


def show_statistics():
     if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

     total = 0
     courses = {}

     with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                name, roll, course = line.strip().split(",")

                total += 1

                course_key = course.strip().lower()

                courses[course_key] = courses.get(course_key, 0) + 1

     print("\n" + "=" * 40)
     print("        STUDENT STATISTICS")
     print("=" * 40)

     print(f"Total Students : {total}")
     print("\nStudents by Course:")

     for course, count in courses.items():
        print(f"{course.title():<25}: {count}")

     print("=" * 40)


def clear_all_students():
    if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

    confirm = input(
        "\n⚠ WARNING: This will delete ALL student records!\n"
        "Are you sure? (y/n): "
    ).lower()

    if confirm == "y":
        with open(FILE_NAME, "w") as file:
            pass

        print("\nAll student records cleared successfully!\n")
    else:
        print("\nClear operation cancelled.\n")

def export_to_csv():
    if not os.path.exists(FILE_NAME):
        print("\nNo Student Records Found!\n")
        return

    students = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                name, roll, course = line.strip().split(",")
                students.append([name, roll, course])

    if not students:
        print("\nNo Student Records Found!\n")
        return

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Roll Number", "Course"])
        writer.writerows(students)

    print("\nStudents exported to students.csv successfully!\n")

    