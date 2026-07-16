from collections import deque, defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = {source}
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for nbr in adj_list[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)

        return False