def trap_rain_water_hard(heights):
    if not heights:
        return
    
    res = 0
    l, r = 0, len(heights) - 1
    left_max, right_max = 0, 0

    while l < r:
        if heights[l] <= heights[r]:
            if heights[l] >= left_max:
                left_max = heights[l]
            else:
                res += left_max - heights[l]
            l += 1
        else:
            if heights[r] >= right_max:
                right_max = heights[r]
            else:
                res += right_max - heights[r]
            r -= 1

    return res
