class Solution:
    def missing_number(self, nums):
        n = len(nums)
        res = 0

        for num in range(n + 1):
            res ^= num

        for num in nums:
            res ^= num

        return res
        