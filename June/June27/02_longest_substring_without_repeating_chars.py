class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        l, longest = 0, 0

        for r, char in enumerate(s):
            if char in char_map and char_map[char] >= l:
                l = char[char_map] + 1
            char_map[char] = r
            longest = max(longest, r - l + 1)

        return longest
    