from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indeg[v] += 1

        queue = deque([node for node in range(numCourses) if indeg[node] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for nbr in graph[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    queue.append(nbr)

        return order[::-1] if len(order) == numCourses else []