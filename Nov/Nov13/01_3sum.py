def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        l, r = i + 1, n - 1

        while l < r:
            s = nums[l] + nums[r]

            if s == target:
                res.append([nums[i], nums[l], nums[r]])


                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

            elif s < target:
                l += 1

            else:
                r -= 1

    return res