class Solution:
    def houseRobber(self, nums):
        prev1, prev2 = 0, 0

        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2 = prev1
            prev1 = curr

        return prev1