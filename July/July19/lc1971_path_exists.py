from collections import defaultdict, deque


class Solution:
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        return self.bfs(graph, source, destination)

    
    def bfs(self, graph, start, destination):
        visited, queue = {start}, deque([start])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        return False