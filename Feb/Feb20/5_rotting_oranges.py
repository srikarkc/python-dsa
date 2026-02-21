from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 1) init: count fresh, enqueue all rotten
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # If no fresh, no time needed
        if fresh == 0:
            return 0

        # If fresh exists but no rotten to start, impossible
        if not q:
            return -1

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2) BFS by levels (each level = 1 minute)
        while q and fresh > 0:
            level_size = len(q)

            for _ in range(level_size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    # rot fresh
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1