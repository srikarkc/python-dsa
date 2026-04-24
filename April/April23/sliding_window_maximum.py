from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq, res = deque(), []
        for i, num in enumerate(nums):
            # 1 - evict expired front
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2 - remove weak elders from the back
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 3 - add young ones to the back
            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result