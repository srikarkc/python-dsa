import heapq

def dijkstra(n, graph, start):
    dist = [float("inf")] * n
    dist[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist+ weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist
