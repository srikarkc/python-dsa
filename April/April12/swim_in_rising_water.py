import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        min_heap = [(grid[0][0], 0, 0)]

        visited = set()
        visited.add((0, 0))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heapq:
            time, r, c = heapq.heappop(min_heap)

            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add(nr, nc)
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(min_heap, (new_time, nr, nc))