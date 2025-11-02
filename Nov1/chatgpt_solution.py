from collections import Counter

def exist(board: list[list[str]], word: str) -> bool:
    if not board or not board[0]:
        return False
    m, n = len(board), len(board[0])

    # 1) Quick frequency pruning
    board_counts = Counter(ch for row in board for ch in row)
    need = Counter(word)
    for ch, cnt in need.items():
        if board_counts[ch] < cnt:
            return False

    # Optional heuristic: search from rarer end first to prune quicker
    # If searching reversed word reduces branching, do it.
    # E.g., if first char is common but last char is rare.
    if board_counts[word[0]] > board_counts[word[-1]]:
        word = word[::-1]

    def dfs(r: int, c: int, k: int) -> bool:
        # k is index in word we are trying to match at (r, c)
        if k == len(word) - 1:
            return board[r][c] == word[k]

        if board[r][c] != word[k]:
            return False

        # Mark as used
        tmp = board[r][c]
        board[r][c] = '#'

        # Explore 4 neighbors
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                if dfs(nr, nc, k + 1):
                    # Restore before returning
                    board[r][c] = tmp
                    return True

        # Restore on backtrack
        board[r][c] = tmp
        return False

    # 2) Try each starting cell that matches word[0]
    first = word[0]
    for i in range(m):
        for j in range(n):
            if board[i][j] == first and dfs(i, j, 0):
                return True
    return False
