# Dijkstra's algorithm

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        # 1 - build graph
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))

        # 2 - min heap
        heap = [(0,k)]      # (time, node)

        # 3 - shortest distances
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = time

            for neighbor, weight in graph[node]:

                if neighbor not in dist:
                    heapq.heappush(heap, (time + weight, neighbor))

        if len(dist) != n:
            return -1
        
        return max(dist.values())