# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums):
        current_sum = best_sum = nums[0]

        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            best_sum = max(current_sum, best_sum)

        return best_sum