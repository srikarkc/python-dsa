class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def isSubTree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)