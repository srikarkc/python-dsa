class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

class Solution:
    def serialize(self, root):
        vals = []
        
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return ','.join(vals)

    def deserialize(self, data):
        tokens = data.split(',')
        i = 0

        def build():
            nonlocal i
            if tokens[i] == '#':
                i += 1
                return None
            
            node = TreeNode(int(tokens[i]))
            i += 1
            node.left = build()
            node.right = build()
            return node

        return build()