class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

# Given BST where all nodes are unique

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur