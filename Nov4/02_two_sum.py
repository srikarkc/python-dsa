def twoSum(nums, target):
    seen = {}   # good to store values as keys and indices as values

    for i, num in enumerate(nums):
        wanted_num = target - num
        if wanted_num in seen:
            return [seen[wanted_num], i]
        seen[num] = i

    return []