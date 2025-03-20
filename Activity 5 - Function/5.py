def divide(a, b):
    """Performs division if the denominator is not zero."""
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiation(a, b):
    """Raises a to the power of b."""
    return a ** b

def remainder(a, b):
    """Finds the remainder if the denominator is not zero."""
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(a, b):
    """Finds the sum of all numbers from a to b (inclusive)."""
    if a > b:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def get_number(prompt):
    """Gets a valid integer from the user."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting program. Goodbye!")
            break
        elif choice in ["D", "E", "R", "F"]:
            num1 = get_number("Enter the first number: ")
            if num1 is None:
                continue
            num2 = get_number("Enter the second number: ")
            if num2 is None:
                continue

            if choice == "D":
                result = divide(num1, num2)
            elif choice == "E":
                result = exponentiation(num1, num2)
            elif choice == "R":
                result = remainder(num1, num2)
            elif choice == "F":
                result = summation(num1, num2)

            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
