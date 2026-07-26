class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1
        return True
    
class Solution:
    def equationsPossible(self, equations):
        uf = UnionFind(26)

        # Step 1 - merge all equations
        for eq in equations:
            if eq[1] == "=":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')   # be careful here its 3 and NOT 2 since a==b b is in position 3
                uf.union(a, b)

        # Step 2- check inequalities
        for eq in equations:
            if eq[1] == "!":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if uf.find('a') == uf.find('b'):
                    return False
        
        return True
