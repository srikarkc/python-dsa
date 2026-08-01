import heapq

def prim(n, graph):
    in_mst = [False] * n
    heap = [(0,0)]
    total, absorbed = 0, 0

    while heap and absorbed < n:
        w, u = heapq.heappop(heap)
        if in_mst(u):
            continue
        in_mst[u] = True
        total += w
        absorbed += 1
        for nw, v in graph[u]:
            if not in_mst[v]:
                heapq.heappush(heap, (nw, v))

    return total if absorbed == n else None
