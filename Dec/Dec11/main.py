from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def bfs(self, root):
        q = deque([root])
        result = []

        while q:
            node = q.popleft()
            result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return result

    def preorder(self, root):
        stack, result = [root], []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def inorder(self, root):
        stack, result = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        
        return result

    def postorder(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]