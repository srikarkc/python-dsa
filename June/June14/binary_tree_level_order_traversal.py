class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque

class Solution:
    def bfs(self, root):

        queue = deque([root])

        result = []

        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level_nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_nodes:
                result.append(level_nodes)

        return result
    