import heapq

class Solution:
    def __init__(self, nums, k):
        self.k = k
        self.heap = []

        for n in nums:
            self.add(n)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]