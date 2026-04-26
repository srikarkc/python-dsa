class Solution:
    def characterReplacement(self, s, k):
        count = {}
        l, maxFreq, best = 0, 0, 0

        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            maxFreq = max(maxFreq, count[ch])

            while (r - l + 1) - maxFreq > k:
                left_ch = s[l]
                count[left_ch] -= 1
                l += 1
            
            best = max(best, r - l + 1)

        return best