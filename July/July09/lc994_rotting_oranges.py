from collections import deque, defaultlist

class Solution:
    def orangesRotting(self, grid):
        queue = deque()
        fresh_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        time = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            queue.append((nr, nc))
            time += 1

        return time if fresh_count == 0 else -1
