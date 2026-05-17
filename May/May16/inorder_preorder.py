class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def constructBtree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        
        self.pre_idx = 0

        value_map = {val: i for i, val in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            inorder_idx = value_map[root_val]

            root.left = build(left, inorder_idx - 1)
            root.right = build(inorder_idx + 1, right)

            return root
        
        return build(0, len(inorder) - 1)
