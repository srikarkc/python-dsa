def two_sum_2(nums, target):
    l, r = 0, len(nums) - 1
    
    while l < r:
        current_sum = nums[l] + nums[r]

        if current_sum == target:
            return [l + 1, r + 1]
        elif current_sum < target:
            l += 1
        else:
            r -= 1
    
    return []