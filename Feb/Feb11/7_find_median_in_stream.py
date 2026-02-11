import heapq

class Solution:
    def __init__(self):
        self.left = []
        self.right = []

    def add(self, num):
        # 1) push to left (as negative)
        heapq.heappush(self.left, -num)

        # 2) move max of left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # 3) rebalance sizes so left >= right
        if len(self.right) > len(self.left):
            heapq.heapppush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2.0