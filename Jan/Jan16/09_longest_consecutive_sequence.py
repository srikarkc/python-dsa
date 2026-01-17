class Solution:
    def longestConsecutiveSequence(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            while (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest