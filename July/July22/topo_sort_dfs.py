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