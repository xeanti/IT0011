A = {"a", "b", "c", "d", "f", "g", "h"}
B = {"b", "c", "h", "i", "l", "m", "o"}
C = {"c", "d", "f", "h", "j", "k"}
U = {"a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"}

AB_intersection = A & B
print("Elements in A and B:", AB_intersection, "Count:", len(AB_intersection))

B_only = B - (A | C)
print("Elements in B that are not in A or C:", B_only, "Count:", len(B_only))

output_sets = {
    "i": (B & A) | (C - A),
    "ii": A & C,
    "iii": A & B,
    "iv": (A & C) - B,
    "v": A & B & C,
    "vi": B - (A | C),
}

for key, value in output_sets.items():
    print(f"{key}: {value}")
