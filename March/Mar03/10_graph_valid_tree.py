from collections import defaultdict

class Solution:
    def graph_valid_tree(self, n, edges):

        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited) == n