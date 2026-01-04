class Solution:
    def houseRobber2(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def robLinear(arr):
            prev1, prev2 = 0, 0

            for x in arr:
                curr = max(prev1, prev2 + x)
                prev2 = prev1
                prev1 = curr
            
            return prev1
        
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))