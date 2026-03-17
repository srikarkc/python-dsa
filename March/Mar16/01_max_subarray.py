class Solution:
    def maxSubArray(self, nums):
        cur_sum = best_sum = nums[0]

        for x in nums[1:]:
            cur_sum = max(x, cur_sum + x)
            best_sum = max(cur_sum, best_sum)

        return best_sum
    