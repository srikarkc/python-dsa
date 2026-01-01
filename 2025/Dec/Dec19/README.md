# Number of Islands

1 represents land and 0 represents water.

Count how many separate islands exist.

All edges are water.

---

Think of each cell as a node. Each land cell connects to its 4 neighbors. An island is one connected component.

Count connected components in a graph.

Start DFS only when the cell is a land cell ("1") - islands += 1. DFS to mark the whole island as visited.

DFS - given one land cell, visit all connected land cells.

DFS Base cases:
    1. Out of bounds
    2. Water ("0")
    3. Already visited

```python
def dfs(r, c):
    # 1. Boundary check
    if r < 0 or r >= ROWS or c < 0  or COLS >= COLS:
        return
    
    # 2. Water check
    if grid[r][c] == 0:
        return

    # 3. Visited check
    if (r, c) in visited:
        return

    # mark visited
    visited.add((r, c))

    # Explore neighbors
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

Now, wrap the above dfs with the outer loop

```python
def numIslands(grid):
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return

        if grid[r][c] == 0:
            return

        if (r, c) in visited:
            return

        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands
```
