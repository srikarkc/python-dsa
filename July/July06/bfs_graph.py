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
