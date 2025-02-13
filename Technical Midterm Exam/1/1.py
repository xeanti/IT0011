def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)

            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {line.strip()} (sum {total}) - {result}")

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except ValueError:
        print("Error: Ensure all lines contain only comma-separated integers.")

process_file("numbers.txt")
