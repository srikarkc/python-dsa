class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0,k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nbr, w in graph[node]:
                nd = d + w
                if nd < dist[nbr]:
                    dist[nbr] = nd
                    heapq.heappush(heap, (nd, nbr))
        
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1