# Undirected
def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if dfs(nbr, node):
                    return True
            elif nbr != parent:
                return True
        return False
    
    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True
        
    return False


# Directed
WHITE, GRAY, BLACK = 0, 1, 2

def has_cycle(n, graph):
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
    
    for node in range(n):
        if color[node] == WHITE and dfs(node):
            return True
        
    return False