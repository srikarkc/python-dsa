class Solution:
    def minCostClimbingStairs(self, cost):
        # in this solution dp[i] = min cost to stand at step i
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        a = cost[0]
        b = cost[1]

        for i in range(2, n):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)

    def minCost(self, cost):
        # dp[i] = min cost to reach step i
        n = len(cost)

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )

        return dp[n]

    # optimized
    def minCostOpt(self, cost):

        a, b = 0, 0

        for i in range(2, len(cost) + 1):
            a, b = b, min(
                b + cost[i - 1],
                a + cost[i - 2]
            )

        return b