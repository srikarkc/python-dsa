class Solution:
    def checkInclusion(self, s1, s2):
        k = len(s1)
        if k > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26

        def idx(ch):
            return ord(ch) - ord('a')
        
        for ch in s1:
            need[idx(ch)] += 1
        
        # first window
        for i in range(k):
            window[idx(s2[i])] += 1

        if window == need:
            return True
        
        # slide
        for r in range(k, len(s2)):
            window[idx(s2[r])] += 1
            window[idx(s2[r - k])] -= 1
            if window == need:
                return True
            
        return False