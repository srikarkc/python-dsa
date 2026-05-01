from collections import deque

def topo_sort(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for nei in graph[node]:
            indegree[nei] = indegree.get(nei, 0) + 1

    queue = deque([node for node in indegree if indegree[node] == 0])

    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return result if len(result) == len(indegree) else []
