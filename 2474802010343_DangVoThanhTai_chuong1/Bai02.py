from sympy import Symbol, solve

x = Symbol('x')

ptb2 = x**2 + 9*x + 8

nghiem = solve(ptb2, x, dict=True)
print("Nghiệm của phương trình x^2 + 9x + 8 = 0 là:")
print(nghiem)
