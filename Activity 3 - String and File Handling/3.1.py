# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Creating a full name
full_name = first_name + " " + last_name

# Slice the first three characters of the first name
name_sliced = first_name[:3]

greeting_message = f"Hello, {name_sliced}! Welcome. You are {age} years old."

print("\nFull Name:", full_name)
print("Sliced Name:", name_sliced)
print("Greeting Message:", greeting_message)
