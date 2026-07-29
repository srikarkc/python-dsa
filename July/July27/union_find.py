class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))     # everyone is their own elder
        self.rank = [0] * n              # tree-height upper bound
        self.count = n                   # live component counter!

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path halving
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False                 # already same clan → cycle edge
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx              # ensure rx is the taller
        self.parent[ry] = rx             # shorter elder bows
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1           # tie → height grows by 1
        self.count -= 1                  # two clans became one
        return True