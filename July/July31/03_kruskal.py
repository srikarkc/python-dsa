def kruskal(n, edges):  # edges w, u, v
    edges.sort()
    uf = UnionFind(n)
    total, used = 0, 0

    for w, u, v in edges:
        if uf.union(u, v):  # False = would close a cycle -> skip
            total += w
            used += 1
            if used == n - 1:
                break

    return total if used == n - 1 else None