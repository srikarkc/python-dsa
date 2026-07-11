from collections import defaultdict
from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # return True if self.bfs(graph, source, destination) else False
        return self.bfs(graph, source, destination)
    
    def bfs(self, graph, start, end):
        visited = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()

            if node == end:
                return True
            
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        
        return False