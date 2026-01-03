# The intuitive solution to this is

# dp[i] should indicate the number of ways to get at step i

# dp[0] and dp[1] should both be 1 since there is 1 way to reach either step 0 or 1

# dp[2] will be 2 which is the sum of dp[0] + dp[1]

# if we follow the above logic, dp[n] = dp[n - 1] + dp[n - 2]

class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]