class Solution:
    def longest_consecutive_sequence(self, nums):
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest