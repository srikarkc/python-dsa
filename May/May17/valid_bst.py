class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

from collections import deque

class Solution:
    def isValidBst(self, root):
        if not root:
            return True
        
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, low, high = q.popleft()

            if not (low < node.val < high):
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return True
    