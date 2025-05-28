import numpy as np

F = np.array([[1, 1],
              [1, 0]], dtype=object)


def fib_matrix_power(k):
    return np.linalg.matrix_power(F, k)

k = 5
Fk = fib_matrix_power(k)

print(f"F^{k} =\n", Fk)

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+2):
        fib.append(fib[-1] + fib[-2])
    return fib

fib_seq = fibonacci(k+1)

print(f"F_{k+1} = {fib_seq[k+1]}")
print(f"F_k = {fib_seq[k]}")
print(f"F_{k-1} = {fib_seq[k-1]}")

print("So sánh với ma trận F^k:")
print(f"Phần tử (0,0) là F_{k+1}:", Fk[0, 0])
print(f"Phần tử (0,1) là F_{k}:", Fk[0, 1])
print(f"Phần tử (1,1) là F_{k-1}:", Fk[1, 1])
