import numpy as np

# Khai báo ma trận 2x2
M1 = np.array([[9, 12], [23, 30]])
print("Ma trận M1:")
print(M1)

# Vector u
u = np.array([2, 1])
print("Vector u:")
print(u)

# Tích ma trận M1 với vector u
tichM1u = M1.dot(u)
print("Tích M1.dot(u):", tichM1u)
# Giải thích: M1 là 2x2, u là vector 2x1, tích cho ra vector 2x1

# Tích vector u với ma trận M1
tichuM1 = u.dot(M1)
print("Tích u.dot(M1):", tichuM1)
# Giải thích: u là vector 1x2, M1 là 2x2, tích cho ra vector 1x2

# Dùng np.dot()
print("np.dot(M1, u):", np.dot(M1, u))  # Tương tự M1.dot(u)
print("np.dot(u, M1):", np.dot(u, M1))  # Tương tự u.dot(M1)

# Tạo ma trận 5x5 toàn 0
mat1 = np.zeros([5,5])
print("mat1 (zeros 5x5):")
print(mat1)

# Ma trận 5x5 toàn 1
mat2 = np.ones([5,5])
print("mat2 (ones 5x5):")
print(mat2)

# Cộng ma trận: mat3 = mat1 + 2 * mat2
mat3 = mat1 + 2 * mat2
print("mat3 = mat1 + 2*mat2:")
print(mat3)

# Gán mat4 tham chiếu đến mat3
mat4 = mat3
# Thay đổi một phần tử mat3
mat3[3][2] = 10
print("mat3 sau khi sửa phần tử [3][2] = 10:")
print(mat3)
print("mat4 sau khi mat3 thay đổi:")
print(mat4)
# mat4 cũng thay đổi vì cùng tham chiếu với mat3

# Sao chép mat3 sang mat5
mat5 = np.copy(mat3)
mat3[3][2] = 20
print("mat3 sau khi sửa phần tử [3][2] = 20:")
print(mat3)
print("mat4 sau khi mat3 thay đổi:")
print(mat4)
print("mat5 sau khi mat3 thay đổi:")
print(mat5)
# mat5 không thay đổi vì là bản sao độc lập

# Ma trận rỗng chưa khởi tạo giá trị cụ thể
mat6 = np.empty([4, 5])
print("mat6 (empty 4x5):")
print(mat6)

# Ma trận đơn vị 4x4
mat7 = np.identity(4)
print("mat7 (identity 4x4):")
print(mat7)

# Ma trận ngẫu nhiên 4x5
mat8 = np.random.random([4, 5])
print("mat8 (random 4x5):")
print(mat8)
