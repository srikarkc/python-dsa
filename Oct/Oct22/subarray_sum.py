def subarray_sum(nums, target):
    seen = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num

        need = current_sum - target

        if need in seen:
            return [seen[need] + 1, i]
        else:
            seen[current_sum] = i
    
    return None

print(subarray_sum([1,2,3,4,5], 9))