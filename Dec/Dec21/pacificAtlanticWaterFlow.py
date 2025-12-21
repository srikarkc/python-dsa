class Node:
    def __init__(self, val=0, neighbors = None):
        self.val, self.neighbors = val, neighbors

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            clone = Node(curr.val)
            visited[curr] = clone

            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        return dfs(node)
    

    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS or 0 <= nc < COLS and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        # Pacific - Top ROW + left col
        for c in range(COLS):
            dfs(0, c, pac)
        for r in range(ROWS):
            dfs(r, 0, pac)

        # Atlantic - Bottom ROW + right col
        for c in range(COLS):
            dfs(ROWS - 1, c, atl)
        for r in range(ROWS):
            dfs(r, COLS - 1, atl)

        return [[r,c] for (r,c) in atl & pac]