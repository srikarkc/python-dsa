class Solution:
    def maximumProduct(self, nums):
        cur_max = cur_min = ans = nums[0]

        for x in nums[1:]:
            a = cur_max * x
            b = cur_min * x

            cur_max = max(x, a, b)
            cur_min = min(x, a, b)

            ans = max(ans, cur_max)

        return ans