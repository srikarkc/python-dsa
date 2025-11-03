def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            num = remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            path.append(num)

            backtrack(path, new_remaining)

            path.pop()

    backtrack([], nums)
    return result