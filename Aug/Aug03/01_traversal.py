from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    dist = {start: 0}

    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
                dist[nbr] = dist[node] + 1

    return dist

def bfs_levels(graph, start):
    visited = {start}
    queue = deque([start])
    levels = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        levels += 1

    return levels

def dfs(graph, node, visited):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph, nbr, visited)

def dfs_iter(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                stack.append(nbr)
