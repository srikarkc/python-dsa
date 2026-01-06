class Solution:
    def coinChange(s, coins, amount):
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], dp[x - c] + 1)

        return dp[amount] if dp[amount] != INF else -1