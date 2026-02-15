class Solution:
    def partition(self, s):
        res, path = [], []
        n = len(s)

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(start):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                if is_pal(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()
        
        backtrack(0)
        return res
    