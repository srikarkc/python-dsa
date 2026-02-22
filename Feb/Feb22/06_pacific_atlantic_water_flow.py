class Solution:
    def PacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pac, atl = set(), set()

        def dfs(r, c, visited):
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        # Pacific
        for r in range(rows):
            dfs(r, 0, pac)
        for c in range(cols):
            dfs(0, c, pac)

        # Atlantic
        for c in range(cols):
            dfs(rows - 1, c, atl)
        for r in range(rows):
            dfs(r, cols - 1, atl)

        return [[r,c] for (r,c) in pac & atl]