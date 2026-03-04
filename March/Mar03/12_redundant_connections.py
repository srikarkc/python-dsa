class Solution:
    def findRedundantConnection(self, edges):
        parent = {}

        for u, v in edges:
            parent[u] = v
            parent[v] = u

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            
            parent[rootY] = rootX
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]