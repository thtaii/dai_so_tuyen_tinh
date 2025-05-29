from sympy import Symbol, solve

# Khai báo biến
x = Symbol('x')
y = Symbol('y')

# Khai báo 2 phương trình dạng biểu thức = 0
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

# Giải hệ phương trình, trả về dạng list dict
nghiem = solve((pt1, pt2), (x, y), dict=True)
print("Nghiệm hệ phương trình:")
print(nghiem)

# Lấy nghiệm đầu tiên (nếu có nhiều nghiệm)
ng = nghiem[0]

# Thay nghiệm vào từng phương trình để kiểm tra
check_pt1 = pt1.subs({x: ng[x], y: ng[y]})
check_pt2 = pt2.subs({x: ng[x], y: ng[y]})

print("Thay nghiệm vào pt1 =", check_pt1)  # Phải bằng 0
print("Thay nghiệm vào pt2 =", check_pt2)  # Phải bằng 0

