import numpy as np

# 1. Dữ liệu mẫu (có thể thay thế bằng dữ liệu thật) ====
A = np.array([[0, 1, 2], [1, 0, 1], [2, 2, 1]])
B = np.array([[1, 2, 0], [2, 1, 1], [0, 0, 2]])
C = np.array([[0, 1, 1], [2, 1, 0], [1, 2, 2]])
D = np.array([[1, 0, 2], [2, 1, 1], [0, 1, 2]])
E = np.array([[0, 1, 2], [2, 0, 1], [1, 2, 0]])

# 2. Từ điển điểm số ====
score_dict = {
    'A': {0: 1, 1: 2, 2: 3},
    'B': {0: 1, 1: 2, 2: 4},
    'C': {0: 0, 1: 1, 2: 2},
    'D': {0: 1, 1: 2, 2: 3},
    'E': {0: 2, 1: 3, 2: 5}
}

# 3. Hàm quy đổi điểm nguy cơ ====
def map_scores(matrix, scores):
    return np.vectorize(lambda x: scores[x])(matrix)

# 4. Tính điểm nguy cơ từng nhóm ====
score_A = map_scores(A, score_dict['A'])
score_B = map_scores(B, score_dict['B'])
score_C = map_scores(C, score_dict['C'])
score_D = map_scores(D, score_dict['D'])
score_E = map_scores(E, score_dict['E'])

# 5. Tổng điểm nguy cơ toàn bộ ====
total_score = score_A + score_B + score_C + score_D + score_E

# 6. Hàm in ra các vị trí thỏa điều kiện ====
def print_positions(condition, title):
    print(f"\n{title}")
    positions = np.argwhere(condition)
    if positions.size == 0:
        print("Không có vị trí nào thỏa mãn.")
    else:
        for pos in positions:
            print(f"Vị trí: ({pos[0]+1}, {pos[1]+1})")

# 7. Các điều kiện ====

# a) An toàn ngắn hạn
print_positions(score_E <= 5, "a. An toàn ngắn hạn")

# b) An toàn tập luyện
print_positions((score_E <= 5) & (score_D <= 2), "b. An toàn tập luyện")

# c) An toàn mùa khô
print_positions((score_A <= 1) & (score_C <= 2) & (score_D <= 2), "c. An toàn mùa khô")

# d) An toàn mùa mưa
print_positions((score_B <= 2) & (score_C <= 2) & (score_D <= 2), "d. An toàn mùa mưa")

# e) An toàn 8 tháng
print_positions((score_A <= 3) & (score_B <= 4) & (score_C <= 5) & (score_D <= 4) & (score_E <= 10), "e. An toàn 8 tháng")
