class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if not node:
        return None
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


# BFS traversal

from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Preorder iterative DFS
def preorder_iterative(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()

        print(node.val)

        # Right first so left gets processed first
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)