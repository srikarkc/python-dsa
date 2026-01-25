class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)

        def hours_needed(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            return total
        
        while l < r:
            mid = (l + r) // 2
            if hours_needed(mid) <= h:
                r = mid
            else:
                l = mid + 1

        return l