# template
from collections import deque
def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()

        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# bfs on trees
def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# bfs on graphs
# we will need cycle detection and the shortest path
# visited set is mandatory
def dfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

# bfs on grid
# number of islands, rotting oranges, & shortest path in binary matrix
def dfs(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(r, c)])
    visited = set([(r, c)])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if (0 <= nx < rows and
                0 <= ny < cols and 
                (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny))