class Solution:
    def twoIntegerSum2(self, nums, target):
        l , r = 0, len(nums) - 1

        while l < r:
            cur_sum = nums[l] + nums[r]

            if target == cur_sum:
                # Remember to return 1-indexed values
                return [l + 1, r + 1]
            
            elif cur_sum < target:
                l += 1
            else:
                r -= 1

        return []