WHITE, GRAY, BLACK = 0, 1, 2

def has_cycle_directed(n, graph):
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for nbr in graph[node]:
            if color[nbr] == GRAY:
                return True
            if color[nbr] == WHITE and dfs(nbr):
                return True
        color[node] = BLACK
        return False
    
    return any(color[v] == WHITE and dfs(v) for v in range(n))
