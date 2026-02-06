class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0 # points to the next root in preorder

        def helper(in_left, in_right):
            nonlocal pre_idx
            if in_left > in_right:
                return None
            
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root.val)

            mid = idx_map[root_val]

            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root
        
        return helper(0, len(inorder) - 1)