class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True
    
class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        dsu = DSU(n)

        for a, b in edges:
            if not dsu.union(a,b):
                return False
            
        return True