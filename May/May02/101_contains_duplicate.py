class Solution:
    def hasDuplicate(self, nums):
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)

        return False