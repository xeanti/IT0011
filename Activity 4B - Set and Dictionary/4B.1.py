A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'j', 'k'}

# (a) Number of elements in A union B
num_A_union_B = len(A | B)
print("Number of elements in A ∪ B:", num_A_union_B)

# (b) Elements in B that are not in A or C
B_not_A_C = B - (A | C)
print("Elements in B that are not in A or C:", B_not_A_C)

# (c) Set operations
h_i_j_k = B | C
c_d_f = A & C
b_c_h = B & (A | C)
d_f = (A & C) - B
c_only = A & B & C
l_m_o = B - (A | C)

print("[h, i, j, k]:", h_i_j_k)
print("[c, d, f]:", c_d_f)
print("[b, c, h]:", b_c_h)
print("[d, f]:", d_f)
print("[c]:", c_only)
print("[l, m, o]:", l_m_o)
