def has_cycle_undirected(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if dfs(nbr, node):          # pass MYSELF as nbr's parent
                    return True             # bubble the alarm up
            elif nbr != parent:             # visited AND not my rope
                return True                 # 🚨 cycle
        return False

    for node in range(n):                   # Topic 5 wrapper — disconnected!
        if node not in visited:
            if dfs(node, -1):               # roots have no parent
                return True
    return False