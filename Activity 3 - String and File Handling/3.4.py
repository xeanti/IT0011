try:
    with open("students.txt", "r") as file:
        # Retrieve and display the file contents
        student_data = file.read()
        print("Student Information:\n")
        print(student_data)

except FileNotFoundError:
    print("Error: Unable to locate 'students.txt'. Please verify that the file exists before attempting to read.")
