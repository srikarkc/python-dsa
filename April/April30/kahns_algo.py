from collections import defaultdict, deque

def topo_sort(num_nodes, edges):
    adj = defaultdict(list)
    indegree = [0] * num_nodes
    
    for u, v in edges:           # edge u → v means u before v
        adj[u].append(v)
        indegree[v] += 1
    
    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return result if len(result) == num_nodes else []  # [] = cycle