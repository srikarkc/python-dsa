class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for x in range(2, n + 1):
            dp[n] = dp[n - 1] + dp[n - 2]

        return dp[n]
    
    # Space-optimization
    def climbStairsOptimized(self, n):
        if n <= 1:
            return 1
        
        prev1, prev2 = 1, 1

        for x in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1