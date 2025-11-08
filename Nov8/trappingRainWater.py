def trappingRainWater(height):
    # This solution takes O(n) space and has a time complexity of O(n)
    n = len(height)
    if n == 0:
        return 0
    
    Lmax = Rmax = [0] * n

    Lmax[0] = height[0]
    for i in range(1, n):
        Lmax[i] = max(Lmax[i - 1], height[i])

    Rmax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        Rmax[i] = max(Rmax[i + 1], height[i])

    water = 0
    for i in range(n):
        water += max(0, min(Lmax[i], Rmax[i]) - height[i])
    
    return water


# Optimal O(n) time complexity sol'n with O(1) space

def optimalTrapWater(height):
    n = len(height)
    l, r = 0, n - 1
    left_max = right_max = 0
    water = 0

    while l < r:
        if height[l] >= height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                water += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                water += right_max - height[r]
            r -= 1

    return water