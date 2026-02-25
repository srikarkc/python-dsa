edges = [[1,2],[1,3],[3,4],[2,4]]

parent = {}

for u, v in edges:
    parent[u] = u
    parent[v] = v

print(parent)