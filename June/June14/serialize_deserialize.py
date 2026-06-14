class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque

class Solution:
    def serialize(self, root):
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                result.append("null")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        vals = data.split(",")
        if vals[0] == "null":
            return None
        
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1

        while i < len(vals):
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root
