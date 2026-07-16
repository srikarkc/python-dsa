from collections import defaultdict

def count_components(n, edges):
    graph = defaultdict(list)              # Topic 2 ritual
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    for node in range(n):                  # range(n), NEVER graph.keys()!
        if node not in visited:
            count += 1                     # dry spot = new island
            dfs(graph, node, visited)      # pour paint (Topic 4 code, unchanged)
    return count

def dfs(graph, node, visited):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph, nbr, visited)