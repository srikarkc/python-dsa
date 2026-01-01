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
    if not height:
        return 0
    
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res