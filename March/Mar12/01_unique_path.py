class Solution:
    def unique_path(self, m, n):
        dp = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c - 1] + 1

        return dp[-1]