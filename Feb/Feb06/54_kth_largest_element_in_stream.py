# Keep a min-heap of size k containing the k largest numbers seen so far

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for x in nums:
            self.add(x)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)
        return self.heap[0]
