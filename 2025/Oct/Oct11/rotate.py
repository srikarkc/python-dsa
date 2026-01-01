def rotate(nums, k):
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums

# The above solution time complexity is O(k * n)

def rotate_optimized(nums, k):
    k = k % len(nums)   # ensures that rotation doesn't exceed the length of the list
    nums[:] = nums[-k:] + nums[:-k]
