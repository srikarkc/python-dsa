class Solution:
    def combinationSum(self, nums, target):
        result = []

        def backtrack(start, path, total):
            if target == total:
                result.append(nums[:])
                return
            
            if target > total:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])

                # backtrack i and not i + 1 because reuse is allowed
                backtrack(i, path, total + nums[i])

                path.pop()

        backtrack(0, [], 0)

        return result