import numpy as np

# Problem 1: Tìm điểm giao giữa hai đường thẳng trong R²

A1 = np.array([[1, 1],
               [2, -1]])
b1 = np.array([5, 4])

sol1 = np.linalg.solve(A1, b1)
print("Problem 1 - Giao điểm hai đường thẳng trong R²:", sol1)

# Problem 2: Tìm giao điểm giữa ba mặt phẳng trong R³

A2 = np.array([[1, 1, 1],
               [2, -1, 1],
               [1, -2, 3]])
b2 = np.array([6, 3, 14])

sol2 = np.linalg.solve(A2, b2)
print("Problem 2 - Giao điểm ba mặt phẳng trong R³:", sol2)

# Problem 3: Tìm hệ số đa thức để đa thức thỏa các nghiệm

roots = [1, 2, 3]
coeffs = np.poly(roots)
print("Problem 3 - Hệ số đa thức có nghiệm 1, 2, 3:", coeffs)


# Problem 4: Phân rã đa thức để tính tích phân

from sympy import symbols, apart, integrate, simplify

x = symbols('x')
expr = (x**2 + 3*x + 2)/(x**2 + x)

partial = apart(expr)
print("Problem 4 - Phân tích thành phân thức đơn:", partial)

integral = integrate(partial, x)
print("Problem 4 - Tích phân của biểu thức:", integral)
