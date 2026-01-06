class Solution:
    def palindromic_substrings(self, s):
        
        def expand_linear(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += expand_count(i, i)
            ans += expand_count(i, i + 1)
        
        return ans