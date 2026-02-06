class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def maxPathSum(self, root):
        best = float("-inf")

        def gain(node):
            nonlocal best
            if not node:
                return 0
            
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))

            best = max(best, node.val + left + right)

            return node.val + max(left, right)
        
        gain(root)
        return best