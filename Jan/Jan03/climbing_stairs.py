class Solution:
    def climbStairs(self, n):
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)