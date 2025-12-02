# BFS - iterative

from collections import deque

def level_order(root):
    if not root:
        return []
    
    q = deque([root])
    res = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(level)
    
    return res


###

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Pattern 1 - DFS return something
def maxDepth(root):
    if not root:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)

def dfs(node):
    if not node:
        #return <base_value>
        return None

    left, right = dfs(node.left), dfs(node.right)

    #return <something>
    return None



# Pattern 2 - DFS with outer self.ans / nonlocal ans
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.ans
    
"""
class Solution:
    def someTreeProblem(self, root):
        self.ans = <initial>

    def dfs(node):
        if not node:
            return <base>
        
            left = dfs(node.left)
            right = dfs(node.right)

        return <something to parent>
    
    dfs(root)
    return self.ans
"""