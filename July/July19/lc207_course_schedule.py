class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        # build directed graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)


        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * numCourses


        def dfs(course):

            # found a back edge
            if color[course] == GRAY:
                return False

            # already verified this subtree
            if color[course] == BLACK:
                return True


            # enter recursion stack
            color[course] = GRAY


            for nxt in graph[course]:
                if not dfs(nxt):
                    return False


            # leave recursion stack
            color[course] = BLACK

            return True



        for course in range(numCourses):
            if not dfs(course):
                return False

        return True