class Solution:
    def rob(self, nums):
        prev1, prev2 = 0, 0

        for n in nums:
            curr = max(prev1, prev2 + n)
            prev2, prev1 = prev1, curr

        return prev1
    