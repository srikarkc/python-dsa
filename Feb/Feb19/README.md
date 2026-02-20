# Graphs

Graphs are an important data structure.

There are 3 types:

1. Undirected
2. Directed
3. Weighted

Graphs can be represented in the following ways:

1. Adjacency list
2. Adjacency matrix

## Graph traversal

1. Depth-first search

```python
def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    print(node.val)

    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

dfs("A", graph, set())

```

2. Breadth-first search

```python
from collections import deque
def bfs(start, graph):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in queue.popleft():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
