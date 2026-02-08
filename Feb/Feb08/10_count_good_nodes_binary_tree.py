class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def goodNodes(self, root):
        def dfs(node, path_max):
            if not node:
                return 0
            
            good = 1 if node.val >= path_max else 0
            path_max = max(path_max, node.val)

            return good + dfs(node.left, path_max) + dfs(node.right, path_max)
        
        return dfs(root, root.val)