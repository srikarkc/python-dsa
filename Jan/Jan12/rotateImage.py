class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # 1 - Transpose matrix
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # 2 - Reverse row
        for r in range(n):
            matrix[r].reverse()