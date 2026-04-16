class Soln:
    def lcs(self, nums):
        longest = 0
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while (num + 1) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest