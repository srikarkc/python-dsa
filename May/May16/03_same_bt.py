class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        queue_p, queue_q = deque([p]), deque([q])

        while queue_p and queue_q:
            nodeP = queue_p.popleft()
            nodeQ = queue_q.popleft()

            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False
            
            queue_p.append(nodeP.left)
            queue_p.append(nodeP.right)
            queue_q.append(nodeQ.left)
            queue_q.append(nodeQ.right)

        return True
    