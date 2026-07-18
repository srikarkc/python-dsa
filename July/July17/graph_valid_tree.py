from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

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