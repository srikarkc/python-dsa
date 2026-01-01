class TrieNode:
    def __init__(self):
        self.children, self.word = {}, None

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            ch = board[r][c]
            if ch not in parent.children:
                return
            node = parent.children[ch]
            if node.word:
                res.append(node.word)
                node.word = None
            board[r][c] = '#'

            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, node)
            if r + 1 < ROWS and board[r + 1][c] != '#':
                dfs(r + 1, c, node)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, node)
            if c + 1 < COLS and board[r][c + 1] != '#':
                dfs(r, c + 1, node)
            
            board[r][c] = ch

            # Prune
            if not node.children and node.word is None:
                del parent.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        
        return res