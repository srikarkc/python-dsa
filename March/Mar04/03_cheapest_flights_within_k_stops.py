# Bellman Ford solution

from math import inf

class Solution:
    def cheapest_flight(self, n, k, flights, src, dest):
        dist = [inf] * n
        dist[src] = 0

        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] != inf and dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp

        return -1 if dist[dest] == inf else dist[dest]
    