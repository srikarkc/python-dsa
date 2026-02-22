class Solution:
    def maxArea(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )
        
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    best = max(best, dfs(r,c))

        return best