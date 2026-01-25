class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums - 1)

        while l < r:
            mid = (l + r) // 2

            # This means the mid is in the left half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]