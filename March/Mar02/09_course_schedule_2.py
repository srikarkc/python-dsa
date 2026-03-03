from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        courses = []

        while q:
            course = q.popleft()
            courses.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return courses if len(courses) == numCourses else []
