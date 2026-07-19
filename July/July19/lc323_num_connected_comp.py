from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0

        for node in range(n):
            if node not in visited:
                count += 1
                self.dfs(graph, node, visited)

        return count

    def dfs(self, graph, node, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                self.dfs(graph, nbr, visited)
