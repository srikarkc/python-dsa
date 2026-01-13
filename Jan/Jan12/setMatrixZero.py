class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])

        firstRowZero = any(matrix[0][c] == 0 for c in range(n))
        firstColZero = any(matrix[0][c] == 0 for c in range(m))

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if firstRowZero:
            for c in range(n):
                matrix[0][c] = 0

        if firstColZero:
            for r in range(m):
                matrix[r][0] = 0
                