from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    distance = {start: 0}

    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
                distance[nbr] = distance[node] + 1
    
    return distance

def bfs_levels(graph, start):
    visited, queue, levels = {start}, deque([start]), 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        levels += 1

    return levels