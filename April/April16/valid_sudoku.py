from collections import defaultdict

class Soln:
    def valid_sudoku(self, board):
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                box = (r // 3, c // 3)

                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True