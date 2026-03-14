class Solution:
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0
        if (target + total_sum) % 2 != 0:
            return 0
        
        subset_sum = (target + total_sum) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]