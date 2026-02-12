def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            # choose
            path.append(nums[i])

            # explore
            backtrack(i + 1, path)

            # undo (backtrack)
            path.pop()

    backtrack(0, [])

    return result