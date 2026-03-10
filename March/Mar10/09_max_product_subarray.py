class Solution:
    def max_product_subarray(self, nums):
        cur_max = cur_min = ans = nums[0]

        for x in nums[1:]:
            a = x * cur_max
            b = x * cur_min

            cur_max = max(x, a, b)
            cur_min = min(x, a, b)

            ans = max(ans, cur_max)

        return ans