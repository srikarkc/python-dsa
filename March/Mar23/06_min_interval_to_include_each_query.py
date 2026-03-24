import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        sorted_q = sorted(enumerate(queries), key=lambda x:x[1])
        ans = [-1] * len(queries)
        heap = []
        i = 0

        for idx, q in sorted_q:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop()

            if heap:
                ans[idx] = heap[0][0]

        return ans