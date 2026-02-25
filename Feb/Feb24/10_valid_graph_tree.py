from collections import defaultdict

class Solution:
    def valid_graph_tree(self, n, edges):

        # Step 1 - Edge count check
        if len(edges) != n - 1:
            return False
        
        # Step 2 - build adjacency list
        graph = defaultdict(list)
        for a,b in edges:
            graph[b].append(a)
            graph[a].append(b)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited) == n
