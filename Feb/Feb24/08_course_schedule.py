from collections import defaultdict, deque

class Solution:
    def courseSchedule(self, numCourses, prerequisites):

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses