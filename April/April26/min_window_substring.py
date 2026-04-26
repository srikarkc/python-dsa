from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""
        
        need = Counter(t)
        required = len(need)

        window = defaultdict(int)
        have = 0

        best = (float('inf'), 0, 0)
        l = 0

        for r, c in enumerate(s):
            # GROW
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1

            # SHRINK
            while have == required:
                # Update best
                if (r - l + 1) < best[0]:
                    best = (r - l + 1, l, r)

                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1

        length, l, r = best
        return "" if length == float("inf") else s[l:r + 1]
            