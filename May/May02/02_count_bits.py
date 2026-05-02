class Solution:
    def countBits(self, n):
        count = [0] * (n + 1)

        for i in range(1, n + 1):
            count[i] = count[i >> 1] + (i & 1)

        return count