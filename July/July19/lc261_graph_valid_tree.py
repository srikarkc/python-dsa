from collections import deque, defaultdict

class Solution:
    def validTree(self, n, edges):
        
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited) == n