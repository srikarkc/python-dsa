# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        value_map = {value: i for i, value in enumerate(inorder)}

        self.pre_idx = 0

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