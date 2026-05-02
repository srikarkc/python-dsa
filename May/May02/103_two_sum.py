class Solution:
    def twoSum(self, nums, target):
        numMap = {}

        for i, num in enumerate(nums):
            wanted = target - num

            if wanted in numMap:
                return [numMap[wanted], i]

            numMap[num] = i