from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = {}

        have = 0
        need_types = 0

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_types:

                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return "" if res_len == float("inf") else s[l:r+1]
    