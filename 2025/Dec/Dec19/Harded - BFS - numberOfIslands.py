from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(sr, sc):
        q = deque([sr, sc])
        visited.add((sr, sc))

        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands