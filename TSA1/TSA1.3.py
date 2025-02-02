print("Pattern A:")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()

print("\nPattern B:")

i = 1
while i <= 5:
    num = (i * 2) - 1
    j = 1
    while j <= num:
        print(num, end="")
        j += 1
    print()
    i += 1
