from collections import defaultdict, deque

def topo_sort(n, edges):  # (a, b) mean a before b
    graph = defaultdict(list)
    indeg = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indeg[b] += 1

    queue = deque([node for node in range(n) if indeg[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph[node]:
            indeg[nbr] -= 1
            if indeg[nbr] == 0:
                queue.append(nbr)

    return order if len(order) == n else []

def topo_sort_dfs(n, graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    order = []                                      # NEW

    def dfs(node):
        color[node] = GRAY
        for nbr in graph[node]:
            if color[nbr] == GRAY: return False     # cycle → abort all
            if color[nbr] == WHITE and not dfs(nbr): return False
        color[node] = BLACK
        order.append(node)                          # NEW: append at finish
        return True

    for v in range(n):
        if color[v] == WHITE and not dfs(v):
            return []
    return order[::-1]                              # NEW: your .reverse()!