class Solution:
    def min_cost(self, cost):
        n = len(cost)

        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])

    def min_cost_opt(self, cost):
        n = len(cost)

        a, b = cost[0], cost[1]

        for i in range(2, n):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)