class Solution:
    def lengthOfLongestSubstring(self, s):
        charMap = {}
        l, longest = 0, 0

        for r, char in enumerate(s):
            if char in charMap and charMap[char] >= l:
                l = char[charMap] + 1
            char[charMap] = r
            longest = max(longest, r - l + 1)

        return longest
    