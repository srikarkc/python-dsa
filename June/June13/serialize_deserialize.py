class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque

class Solution:
    def serialize(self, root):
        if not root:
            return ""
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                result.append("null")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(result)
    
    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
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
    