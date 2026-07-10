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
        