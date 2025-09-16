# Solve reverse for doubly linked list

# Reverse between

Good luck remembering this in an interview, lol

```python
for _ in range(end_index - start_index):
    node_to_move = current.next

    current.next = node_to_move.next
    if node_to_move.next:
        node_to_move.next.prev = current
    
    node_to_move.next = prev.next
    prev.next.prev = node_to_move
    prev.next = node_to_move
    node_to_move.prev = prev
```