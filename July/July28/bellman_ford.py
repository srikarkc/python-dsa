def bellman_ford(n, edges, src):           # edges: list of (u, v, w)
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(n - 1):                 # V-1 rounds
        updated = False
        for u, v, w in edges:              # relax EVERY edge — no graph build needed!
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:                    # early convergence — free optimization
            break

    for u, v, w in edges:                  # round V: the negative-cycle probe
        if dist[u] + w < dist[v]:
            return None                    # 🚨 negative cycle reachable from src
    return dist