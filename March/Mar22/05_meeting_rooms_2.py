import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)

        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            current = intervals[i]

            if current.start >= min_heap[0]:
                heapq.heappush(min_heap)

            heapq.heappush(min_heap, current.end)

        return len(min_heap)