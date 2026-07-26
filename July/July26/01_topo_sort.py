from collections import defaultdict, deque

def topo_sort(n, edges):    # edges - (a,b) means a before b
    graph = defaultdict(list)
    indeg = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1

    queue = deque([node for node in range(n) if indeg[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph[node]:
            indeg[nbr] -= 1
            if indeg[nbr] == 0:
                queue.append(nbr)

    return order