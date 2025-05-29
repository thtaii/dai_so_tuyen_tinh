from sympy import Symbol, solve

x = Symbol('x')

# Phương trình 1: x + 3 = 5
bieuthuc1 = x + 3 - 5
nghiem1 = solve(bieuthuc1)
print("Nghiệm của x + 3 = 5:", nghiem1)

# Phương trình 2: x^2 + 3 - 5 = 0
bieuthuc2 = x**2 + 3 - 5
nghiem2 = solve(bieuthuc2)
print("Nghiệm của x^2 + 3 - 5 = 0:", nghiem2)
print("Nghiệm 1:", nghiem2[0])
print("Nghiệm 2:", nghiem2[1])
