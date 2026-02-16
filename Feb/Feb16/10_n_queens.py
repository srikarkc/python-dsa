class Solution:
    def solveNQueens(self, n):
        res = []
        cols = set()
        diag = set()
        anti = set()

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti:
                    continue

                cols.add(c)
                diag.add(r - c)
                anti.add(r + c)

                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."

                cols.remove(c)
                diag.remove(r - c)
                anti.remove(r + c)

        backtrack(0)
        return res