from collections import deque

class Solution:
    def islandsAndTreasures(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        queue = deque()

        # Step 1: Add all treasures to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # Step 2: BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = r + dc

                # check bounds
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # only update empty land
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))