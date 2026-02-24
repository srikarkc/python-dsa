from collections import deque

class Solution:
    def surroundedRegions(self, board):
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        q = deque()

        def mark_border(r,c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = '#'
                q.append((r,c))

        # Step 1 - mark border
        for r in range(rows):
            mark_border(r, 0)
            mark_border(r, cols - 1)
        for c in range(cols):
            mark_border(0, c)
            mark_border(rows - 1, c)

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                mark_border(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
