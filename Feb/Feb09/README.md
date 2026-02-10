# Heap and Priority Queue

A heap is a `complete binary tree` that always keeps the *most important* element at the top.

A priority queue is just using a heap to always pull the highest (or lowest) priority item.

## Heap implementation

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print(heap[0])  # 1

print(heapq.heappop(heap))  # 1
```

To implement a max-heap in python --> Use negative numbers.

### Priority queues with tuples

`heapq.heappush(heap, (priority, value))`

