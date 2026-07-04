n = 5
faulty_matrix = [[0] * n] * n
print(faulty_matrix)

faulty_matrix[1][1] = 1

print(faulty_matrix)

matrix = [[0] * n for _ in range(n)]
print("\n")
print(matrix)

matrix[1][1] = 1

print(matrix)