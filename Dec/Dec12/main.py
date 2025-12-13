<<<<<<< HEAD
class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            # Mismatch cases
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if board[r][c] != word[i]:
                return False
            
            # Success case
            if i == len(word) - 1:
                return True
            
            # Choose mark visited
            temp = board[r][c]
            board[r][c] = '#'

            # explore neighbors
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            board[r][c] = temp

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                
        return False
=======
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def bfs(self, root):
        q = deque([root])
        result = []

        while q:
            node = q.popleft()
            result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return result

    def preorder(self, root):
        stack, result = [root], []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def inorder(self, root):
        stack, result = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        
        return result

    def postorder(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]
>>>>>>> 1560b7f2d42844d0d6581d215ee58b5bd5566080
