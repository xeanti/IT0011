# Get user input
last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

# Format and store the collected information
student_info = (
    f"Last Name: {last_name}\n"
    f"First Name: {first_name}\n"
    f"Age: {age}\n"
    f"Contact Number: {contact_number}\n"
    f"Course: {course}\n\n"
)

# Append the information to the file
with open("students.txt", "a") as file:
    file.write(student_info)

# Display confirmation message
print("\nStudent information has been successfully saved to 'students.txt'.")
