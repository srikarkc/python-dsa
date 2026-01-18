class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = set()
        l, max_length = 0, 0

        for r, ch in enumerate(s):
            if ch in chars:
                ch.remove(s[l])
                l += 1
            chars.add(ch)
            max_length = max(max_length, r - l + 1)

        return max_length