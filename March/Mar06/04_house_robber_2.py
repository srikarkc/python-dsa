# Break into 2 halves - exclude the first value and the last value & find max

class Solution:
    def house_robber_2(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(arr):
            rob1, rob2 = 0, 0

            for num in arr:
                rob1, rob2 = rob2, max(rob2, num + rob1)

            return rob2
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))