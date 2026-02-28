from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        print(graph)

        heap = [(0,k)]

sol = Solution()
sol.networkDelayTime(times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1)
