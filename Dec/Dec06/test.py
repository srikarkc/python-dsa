from collections import deque

queue = deque([0])

print(type(queue))

print(queue)

print(f"Popping left: {queue.popleft()}")

print(queue)