import heapq
from collections import defaultdict

def dijkstra(n, edges, src):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v,w))
    dist = [float('inf')] * n
    dist[src] = 0
    heap = [(0,src)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nbr, w in graph[node]:
            nd = d + w
            if nd  < dist[nbr]:
                dist[nbr] = nd
                heapq.heappush(heap, (nd, nbr))

    return dist