class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def maxPathSum(self, root):
        best = float("-inf")

        def dfs(node):
            nonlocal best
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            best = max(best, node.val + left + right)
            return node.val + best(left, right)

        dfs(root)
        return best
