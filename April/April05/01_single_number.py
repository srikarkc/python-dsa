class Solution:
    def single_number(self, nums):
        res = 0
        
        for num in nums:
            res ^= num

        return res