from collections import deque

class Solution:
    def islandsAndTreasures(self, grid):
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # 1 - add all treasures to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        # 2 - use BFS to set distances
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows or 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))