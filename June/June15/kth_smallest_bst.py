class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def kth_smallest(self, root, k):
        count = 0
        result = None

        def inorder(node):
            nonlocal count, result
            if not node or result is not None:
                return
            inorder(node.left)
            count += 1
            if count == k:
                result = node.val
                return
            inorder(node.right)

        inorder(root)
        return result
    