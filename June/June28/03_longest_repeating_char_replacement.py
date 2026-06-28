class Solution:
    def charReplacement(self, s, k):
        counts = {}
        l, max_freq, best = 0, 0, 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_freq = max(max_freq, counts[s[r]])
            window_size = r - l + 1
            if window_size - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)

        return best
    