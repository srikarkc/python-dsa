class Solution:
    def trap_rain_water(self, height):
        if not height:
            return
        
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    res += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1

        return res