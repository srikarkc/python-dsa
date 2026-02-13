class Solution:
    def permutations(self, nums):
        res = []

        def backtrack(path, used):

            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(start, len(nums)):

                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path, used)

                path.pop()
                user[i] = False

        backtrack([], [False] * len(nums))

        return res