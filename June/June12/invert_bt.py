class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def invertBinaryTree(self, root):
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root