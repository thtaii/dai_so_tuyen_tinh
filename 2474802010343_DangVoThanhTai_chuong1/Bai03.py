from sympy import Symbol, solve

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

ptb2 = a*x**2 + b*x + c

# Giải theo biến x, trả về dạng dictionary
nghiem = solve(ptb2, x, dict=True)

print("Nghiệm tổng quát của phương trình a*x^2 + b*x + c = 0 là:")
print(nghiem)
