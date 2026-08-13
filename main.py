from functions import *
show_dashboard()
while True:


    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Sort Students")
    print("7. Filter by Course")
    print("8. Student Statistics")
    print("9. Clear All Students")
    print("10. Export Students to CSV")
    print("11. Exit")
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
       update_student()

    elif choice == "6":
       sort_students()

    elif choice == "7":
       filter_by_course()

    elif choice == "8":
       show_statistics()

    elif choice == "9":
       clear_all_students()

    elif choice == "10":
       export_to_csv()

    elif choice == "11":
       print("Thank You!")
       break
else:
    print("Invalid Choice!")

