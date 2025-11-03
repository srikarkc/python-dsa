def subset(nums):
    result = []

    def backtrack(i, current):
        if len(nums) == i:
            result.append(current[:])
            return
        
        current.append(nums[i])
        backtrack(i+1, current)

        current.pop()
        backtrack(i+1, current)

    backtrack(0, [])
    return result

print(subset([1,2,3]))