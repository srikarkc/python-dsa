from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

# Easy problem1 - Invert Binary Tree
class Solution1:
    def invertBinaryTree(self, root):
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return root
   

# Easy problem2 - Maximum Depth of Binary Tree
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
    

# Easy problem3 - Same Binary Tree
class Solution3:
    def isSameTree(self, p, q):
        queue_p, queue_q = deque([q]), deque([q])

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
    

# Easy problem4 - Subtree of another Tree
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