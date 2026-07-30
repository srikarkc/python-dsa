from collections import deque, defaultdict

def topo_sort(n, edges):                   # edges: (a, b) = a before b
    graph = defaultdict(list)
    indeg = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indeg[b] += 1                      # b gains a prerequisite

    queue = deque(v for v in range(n) if indeg[v] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)                 # doing the task
        for nbr in graph[node]:
            indeg[nbr] -= 1                # crossed off nbr's prereq list
            if indeg[nbr] == 0:            # fully unblocked
                queue.append(nbr)

    return order if len(order) == n else []   # short order = cycle