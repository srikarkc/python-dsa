class Solution:
    def twoSum(self, nums, target):
        num_dict = {}

        for i, n in enumerate(nums):
            num_dict[n] = i

        for i, n in enumerate(nums):
            wanted_num = target - n
            if wanted_num in num_dict and num_dict[wanted_num] != i:
                return [i, num_dict[wanted_num]]
            
    
    # a further optimized solution with only 1 for loop

    def twoSum_optimized(self, nums, target):
        seen = {}

        for i, n in enumerate(nums):
            want = target - n
            if want in seen:
                return [seen[want], i]
            seen[n] = i