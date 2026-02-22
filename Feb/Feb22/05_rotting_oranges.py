from collections import deque

class Solution:
    def rottingOranges(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1 - set q and fresh count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0

        # Step 2 - apply BFS
        while q and fresh > 0:
            level_size = len(q)

            for _ in range(level_size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))

            minutes += 1

        return minutes if fresh == 0 else -1