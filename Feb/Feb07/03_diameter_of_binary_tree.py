class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def diameterTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        return diameter
    
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0    # height = 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter