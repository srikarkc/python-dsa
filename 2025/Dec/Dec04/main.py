from collections import deque
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        # queue stores (node, min allowed value, max allowed value)
        queue = deque([(root, -math.inf, math.inf)])

        while queue:
            node, low, high = queue.popleft()

            # check BST property
            if not (low < node.val < high):
                return False

            # left child → allowed max becomes node.val
            if node.left:
                queue.append((node.left, low, node.val))

            # right child → allowed min becomes node.val
            if node.right:
                queue.append((node.right, node.val, high))

        return True
