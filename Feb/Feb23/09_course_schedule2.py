from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph + indegree
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Start with courses that have no prereqs
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            # "remove" this course and update neighbors
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

            return order if len(order) == numCourses else []
