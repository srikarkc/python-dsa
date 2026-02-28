from math import inf

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [inf] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]
            for u, v, w in flights:
                if dist[u] != inf and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist

        return -1 if dist[dst] == inf else dist[dst]