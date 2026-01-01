# Classic problem for detecting cycles in directed graphs.

# prerequisite = [a, b] means you need to take 'b' before 'a'

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses    # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(course):
            if state[course] == 1:
                return False    # cycle cound
            if state[course] == 2:
                return True     # already processed

            state[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
                
            state[course] = 2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True