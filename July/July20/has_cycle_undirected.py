def has_cycle(n, graph):
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
            if dfs(node, -1):   # roots have no parent
                return True
    
    return False
