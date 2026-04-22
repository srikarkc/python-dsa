class Solution:
    def trap(self, height):
        if not height:
            return
        
        left, right = 0, len(height) - 1
        max_left = max_right = water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                l += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water = max_right - height[right]
                r -= 1

        return water