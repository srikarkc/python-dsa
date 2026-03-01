class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def clone_graph(self, node):
        if not node:
            return None
        
        clones = {}

        def dfs(cur):
            if cur in clones:
                return clones[cur]
            
            copy = Node(cur.val)
            clones[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

        return dfs(node)