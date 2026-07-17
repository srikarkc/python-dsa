WHITE, GRAY, BLACK = 0, 1, 2

def has_cycle_directed(n, graph):
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY                  # entering: I'm on the path now
        for nbr in graph[node]:
            if color[nbr] == GRAY:          # 🚨 someone on my own path
                return True
            if color[nbr] == WHITE and dfs(nbr):
                return True
        color[node] = BLACK                 # leaving: certified clean
        return False

    return any(color[v] == WHITE and dfs(v) for v in range(n))