class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque

class Solution:
    def validateTree(self, root):
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, low, high = q.popleft()

            if not (low < node.val < high):
                return False
            
            if node.left:
                q.append((node.left, node.val, high))
            if node.right:
                q.append((node.right, low, node.val))

        return True
    
