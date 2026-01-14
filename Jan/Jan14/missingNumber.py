class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        res = 0

        for i in range(n + 1):
            res ^= i

        for x in nums:
            res ^= x

        return res
    
    # better solution - 2sum
    def twoSumMissingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
    