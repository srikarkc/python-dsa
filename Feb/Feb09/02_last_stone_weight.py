import heapq

class Solution:
    def lastStoneWeight(self, stones):
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -(y - x))
        
        return -heap[0] if heap else 0