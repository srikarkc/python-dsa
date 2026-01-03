from collections import defaultdict

counts = defaultdict(int)

counts['apple'] = 1
counts['banana'] = 2
counts['apple'] += 2

print(counts)


graph = defaultdict(list)

graph[1].append(2)
graph[1].append(3)
graph[2].append(4)

print(graph)