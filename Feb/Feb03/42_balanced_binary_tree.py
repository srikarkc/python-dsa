class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def balancedBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0        # height of empty tree
            
            left = dfs(node.left)
            if left == -1:
                return -1
            
            right = dfs(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)     # height
        
        return dfs(root) != -1