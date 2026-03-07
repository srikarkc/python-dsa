class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        best_l, best_r = 0, 0

        def expand(l, r):
            nonlocal best_l, best_r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1

            if r - l > best_r - best_l:
                best_r, best_l = r, l

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[best_l:best_r + 1]