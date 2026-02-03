from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def isSameTreeDFS(self, p, q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTreeDFS(p.left, q.left) and self.isSameTreeDFS(p.right, q.right)
        else:
            return False
        
    def isSameTreeBFS(self, p, q):
        if not p and not q:
            return True

        queue_p, queue_q = deque([p]), deque([q])

        while queue_p and queue_q:
            for _ in range(len(queue_p)):
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