class Solution:
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            if grid[r][c] == "0":
                return
            
            if (r, c) in seen:
                return

            seen.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                islands += 1
                dfs(r, c)

        return islands