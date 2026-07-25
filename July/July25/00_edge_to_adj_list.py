from collections import defaultdict

def gen_graph(edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # if the graph is not directional

    return graph

def gen_adj_matrix(n, edges):
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1    # if the graph is not directional

    return matrix
