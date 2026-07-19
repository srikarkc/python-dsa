class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    self.dfs(grid, (r,c), visited)

        return islands

    def dfs(self, grid, coords, visited):
        r, c = coords
        visited.add((r,c))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr,nc) not in visited and grid[nr][nc] == "1":
                coords = (nr, nc)
                self.dfs(grid, coords, visited)