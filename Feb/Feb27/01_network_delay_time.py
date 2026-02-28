from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, k, n):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        dist = {}

        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = time

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + weight, nei))
        
        if len(dist) != n:
            return -1
        
        return max(dist.values())