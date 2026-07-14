def numIslands(grid):
    rows, cols = len(grid), len(grid[0])

    visited, islands = set(), 0

    def dfs(r, c):
        visited.add((r,c))

        directions = [
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == "1"
                and (nr, nc) not in visited
            ):
                dfs(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                islands += 1
                dfs(r, c)

    return islands
