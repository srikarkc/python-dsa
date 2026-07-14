def count_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    for node in range(n):
        if node not in visited:
            count += 1
            dfs(graph, node, visited)

    return count

def dfs(graph, node, visited):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph, nbr, visited)
            