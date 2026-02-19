class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c>= COLS:
                return
            
            if grid[r][c] == "0":
                return
            
            if (r, c) in visited:
                return
            
            visited.add(r, c)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands