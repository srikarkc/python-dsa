from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # 1 - build graph
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # 2 - initialize queue with indegree 0 nodes
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0

        # 3 - BFS
        while queue:
            course = queue.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
    