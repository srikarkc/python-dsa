class Solution:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, height * width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxArea
    