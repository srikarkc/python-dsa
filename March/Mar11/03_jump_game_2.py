class Solution:
    def jump(self, nums):
        jumps, current_end, furthest = 0, 0, 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = furthest

        return jumps
    