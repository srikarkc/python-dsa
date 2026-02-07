class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def maxDepth(self, root):

        def dfs(root):
            if not root:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        
        return dfs(root)



# This is the BFS solution
from collections import deque
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth