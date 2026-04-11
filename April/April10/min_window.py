from collections import Counter

class Solution:
    def min_windows(self, s, t):
        if not s or not t:
            return
        
        need = Counter(t)
        window = {}

        need_count = len(need)
        have = 0

        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                window_len = r - l + 1
                if window_len < res_len:
                    res = [l, r]
                    res_len = window_len
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
            
        l , r = res
        return s[l:r + 1] if res_len != float("inf") else ""