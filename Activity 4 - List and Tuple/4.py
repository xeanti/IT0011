students = []

def show_all_students():
    for student in students:
        print(student)

def get_last_name(student):
    return student[1]

def order_by_last_name():
    sorted_students = sorted(students, key=get_last_name)
    for student in sorted_students:
        print(student)

def compute_grade(student):
    return (0.6 * float(student[2])) + (0.4 * float(student[3]))

def order_by_grade():
    sorted_students = sorted(students, key=compute_grade, reverse=True)
    for student in sorted_students:
        print(student)

def show_student(student_id):
    for student in students:
        if student[0] == student_id:
            print(student)
            return
    print("Student not found.")

def add_record():
    student = (
        input("Enter student ID (6 digits): "),
        input("Enter first name: "), input("Enter last name: "),
        input("Enter class standing grade: "),
        input("Enter major exam grade: ")
    )
    students.append(student)
    print("Student added successfully!")

def edit_record():
    student_id = input("Enter student ID to edit: ")
    for i, student in enumerate(students):
        if student[0] == student_id:
            students[i] = (
                student_id,
                input("Enter new first name: "), input("Enter new last name: "),
                input("Enter new class standing grade: "),
                input("Enter new major exam grade: ")
            )
            print("Student record updated!")
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter student ID to delete: ")
    global students
    students = [student for student in students if student[0] != student_id]
    print("Student deleted successfully!")

def menu():
    while True:
        print("""
        1. Show All Students
        2. Order by Last Name
        3. Order by Grade
        4. Show Student Record
        5. Add Record
        6. Edit Record
        7. Delete Record
        8. Exit
        """)
        choice = input("Enter choice: ")
        if choice == "1":
            show_all_students()
        elif choice == "2":
            order_by_last_name()
        elif choice == "3":
            order_by_grade()
        elif choice == "4":
            show_student(input("Enter student ID: "))
        elif choice == "5":
            add_record()
        elif choice == "6":
            edit_record()
        elif choice == "7":
            delete_record()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Try again.")

menu()
