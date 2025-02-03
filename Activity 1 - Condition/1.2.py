num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            print(f"{num1}, {num2}, {num3}")
        else:
            print(f"{num1}, {num3}, {num2}")
    else:
        print(f"{num3}, {num1}, {num2}")
elif num2 >= num3:
    if num1 >= num3:
        print(f"{num2}, {num1}, {num3}")
    else:
        print(f"{num2}, {num3}, {num1}")
else:
    print(f"{num3}, {num2}, {num1}")
