class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

from collections import deque

class Solution:
    def levelOrderTraversal(self, root):
        if not root:
            return []
        
        queue = deque([root])
        results = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(level)

        return results