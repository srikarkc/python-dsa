# Dynamic Programming 1-D problems

class Solution:
    def climbStairs(self, n):

        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n] 

    # the following solution uses constant space

    def climbStairsOptimized(self, n):

        a, b = 1, 1

        for _ in range(n):
            a, b = b, a + b

        return a


    # the problem is naturally recursive

    def climbStairsSimple(self, n):
        if n <= 1:
            return 1

        return climbStairs(n - 1) + climbStairs(n - 2)
        