# Problem 5 - build from inorder and preorder
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        index_map = {value: i for i, value in enumerate(inorder)}

        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            inorder_idx = index_map[root_val]

            root.left = build(left, inorder_idx - 1)
            root.right = build(inorder_idx + 1, right)

            return root
        
        return build(0, len(inorder) - 1)