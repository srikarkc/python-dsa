from collections import deque

def bfs(graph, start):
    visited = {start}                      # mark WHEN ENQUEUED — see bug #1
    queue = deque([start])
    dist = {start: 0}

    while queue:
        node = queue.popleft()             # deque, NOT list — see bug #2
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)           # claim it immediately
                dist[nbr] = dist[node] + 1
                queue.append(nbr)
    return dist

def bfs_levels(graph, start):
    visited = {start}
    queue = deque([start])
    level = 0
    while queue:
        for _ in range(len(queue)):        # freeze current level's size
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        level += 1                         # entire ring processed
        