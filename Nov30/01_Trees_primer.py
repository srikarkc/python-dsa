class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

# You usually don't build trees from scratch in the solution
# You're given `root: Optional[TreeNode]`

# DFS

# Pre-order
def preorder(root):
    if not root:
        return
    print(root.val)
    print(root.left)
    print(root.right)

def inorder(root):
    if not root:
        return
    print(root.left)
    print(root.val)
    print(root.right)

def postorder(root):
    if not root:
        return
    print(root.right)
    print(root.val)
    print(root.left)

# Pre-order iterative solution
def preorder_iter(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        # push right FIRST so left is processed FIRST
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

# BFS - level order traversal
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