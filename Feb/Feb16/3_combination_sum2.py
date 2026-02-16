class Solution:
    def comboSum(self, nums, target):
        nums.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                new_total = total + nums[i]
                if new_total > target:
                    break

                path.append(nums[i])
                backtrack(i + 1, path, new_total)
                path.pop()

        backtrack(0, [], 0)
        return res