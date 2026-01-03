# In this problem - the houses are in a circle with the first and the last house adjacent to each other

class Solution:
    def houseRobber(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def rob_linear(arr):
            prev2, prev1 = 0, 0
            for x in arr:
                curr = max(prev1 , x + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))