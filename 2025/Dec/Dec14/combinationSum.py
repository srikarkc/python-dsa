class Solution:
    def combinationSum(self, candidates, target):
        results = []
        def backtrack(start, remaining, path):
            if remaining == 0:
                results.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                backtrack(i, remaining - num, path)
                path.pop()
        backtrack(0, target, [])
        return results