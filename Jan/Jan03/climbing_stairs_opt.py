# space optimization

class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return 1
        
        prev2 = 1 # dp[i - 2]
        prev1 = 1 # dp[i - 1]

        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1