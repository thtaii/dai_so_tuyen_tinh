from sympy import symbols, Eq, solve, expand, apart, integrate

# Khai báo biến
x, y, z = symbols('x y z')

# Problem 1: Giao điểm hai đường thẳng trong R²

eq1 = Eq(x + y, 5)
eq2 = Eq(2*x - y, 4)

sol1 = solve((eq1, eq2), (x, y))
print("Problem 1 - Giao điểm hai đường thẳng:", sol1)

# Problem 2: Giao điểm ba mặt phẳng trong R³

eq3 = Eq(x + y + z, 6)
eq4 = Eq(2*x - y + z, 3)
eq5 = Eq(x - 2*y + 3*z, 14)

sol2 = solve((eq3, eq4, eq5), (x, y, z))
print("Problem 2 - Giao điểm ba mặt phẳng:", sol2)

# Problem 3: Tìm hệ số đa thức thỏa các nghiệm x = 1, 2, 3

poly_expr = (x - 1)*(x - 2)*(x - 3)
expanded_poly = expand(poly_expr)
print("Problem 3 - Đa thức thỏa các nghiệm 1, 2, 3:", expanded_poly)

# Problem 4: Phân tích phân thức để tính tích phân

expr = (x**2 + 3*x + 2)/(x**2 + x)

partial = apart(expr)
print("Problem 4 - Phân tích thành phân thức đơn:", partial)

integrated = integrate(partial, x)
print("Problem 4 - Tích phân của biểu thức:", integrated)
