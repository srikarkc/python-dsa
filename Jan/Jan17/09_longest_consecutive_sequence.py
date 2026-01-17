class Solution:
    def lonestConsecutiveSequence(self, nums):
        numsSet = set(nums)
        longest = 0

        for i in nums:
            if (i - 1) not in numsSet:
                length = 1
                while (i + length) in numsSet:
                    length += 1
                longest = max(longest, length)

        return longest