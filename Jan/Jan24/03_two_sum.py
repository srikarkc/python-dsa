class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            wanted_num = target - num
            if wanted_num in seen:
                return [seen[wanted_num], i]
            seen[num] = i
        
        return []