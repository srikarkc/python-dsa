from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

# Problem 1 - Invert binary tree
class Solution1:
    def invertBinaryTree(self, root):
        if not root:
            return
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


# Problem 1 - with recursion
class Solution1_1:
    def invertBinaryTree(self, root):
        if not root:
            return
        
        self.left, self.right = self.right, self.left

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root
    

# Problem 2 - Maximum depth of a binary tree
class Solution2:
    def maxDepth(self, root):
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth
    

# Problem 3 - Same Binary Tree
class Solution3:
    def sameBinaryTree(self, p, q):
        queue_p, queue_q = deque([p]), deque([q])

        while queue_p and queue_q:
            for _ in range(len(queue_p)):
                nodeP, nodeQ = queue_p.popleft(), queue_q.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                
                queue_p.append(nodeP.left)
                queue_p.append(nodeP.right)
                queue_q.append(nodeQ.left)
                queue_q.append(nodeQ.right)

        return True
    

# Problem 4 - Subtree of another tree
class Solution4:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

# Problem 5 - Lowest common ancestor of a binary search tree
class Solution5:
    def lowestCommonAncestor(root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            

# Problem 6 - Binary tree level order traversal
class Solution6:
    def binaryTreeLevelOrderTraversal(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_results = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_results.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_results)

        return result