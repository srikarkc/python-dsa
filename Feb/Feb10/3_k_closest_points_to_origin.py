import heapq

class Solution:
    def kClosestPoints(self, points, k):
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for (_, x, y) in heap]
    