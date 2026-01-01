class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else None

# If a node is already cloned, reuse it. Otherwise, clone it and explore neighbors.

class Solution:
    def cloneGraph(self, node):
        if not node:
            return
        
        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            # Clone the node
            clone = Node(curr.val)
            visited[curr] = clone

            # Clone the neighbors
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone
        
        return visited