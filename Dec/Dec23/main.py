class Solution:
    def validTree(self, n, edges):
        if len(edges) > n + 1:
            return False
        
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
                return True
            
        return dfs(0, -1) and len(visited) == n