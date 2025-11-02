from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int, k: int) -> bool:
            if r < 0 or r >=m or c < 0 or c >= n:
                return False
            if visited[r][c]:
                return False
            if board[r][c] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited[r][c] = True

            if (dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or 
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)):
                visited[r][c] = False
                return True
            
            visited[r][c] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j , 0):
                    return True

        

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

sol1 = Solution()
sol1.exist(board, word)