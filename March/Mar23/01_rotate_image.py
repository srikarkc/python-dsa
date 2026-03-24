class Solution:
    def rotateImage(self, matrix):
        n = len(matrix)

        # 1 - transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2 - reverse the row
        for r in range(n):
            matrix[r].reverse()