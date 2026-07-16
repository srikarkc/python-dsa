def dfs_iter(graph, start):
    visited = set()
    stack = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                stack.append(nbr)
