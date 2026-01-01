from collections import deque

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left, self.rigth = None, None

class Solution:
    def levelOrderTraversal(root):
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res
