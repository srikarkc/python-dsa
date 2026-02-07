class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

from collections import deque

class Solution:
    def sameTree(self, p, q):
        if not p and not q:
            return True
        
        queue_p, queue_q = deque(p), deque(q)

        while queue_p or queue_q:
            for _ in range(len(queue_q)):
                nodeP, nodeQ = queue_p.popleft(), queue_q.popleft()

                if not nodeP and not nodeQ:
                    continue
                if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                    return False
                
                queue_p.append(nodeP.left)
                queue_q.append(nodeQ.left)
                queue_p.append(nodeP.right)
                queue_q.append(nodeQ.right)

        return True