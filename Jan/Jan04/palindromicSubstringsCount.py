class Solution:
    def countSubstrings(s):
        n = len(s)

        def expand_count(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        ans = 0
        for i in range(n):
            ans += expand_count(i, i)
            ans += expand_count(i, i + 1)

        return ans