from collections import deque

class Solution:
    def surrounded_regions(self, board):
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        q = deque()

        def add_border(r,c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "#"
                q.append((r,c))

        for r in range(rows):
            add_border(r,0)
            add_border(r,cols - 1)
        for c in range(cols):
            add_border(0,c)
            add_border(rows - 1,c)

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                q.append(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"