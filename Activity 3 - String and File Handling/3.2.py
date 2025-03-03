# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Creating a full name
full_name = first_name + " " + last_name

# Making the full name uppercase and lowercase
upper_case_name = full_name.upper()
lower_case_name = full_name.lower()

# Calculate the length of the full name (including space)
name_length = len(full_name)

# Display the results
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", upper_case_name)
print("Full Name (Lower Case):", lower_case_name)
print("Length of Full Name:", name_length)
