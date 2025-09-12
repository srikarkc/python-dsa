# Binary to decimal problem

Given a linked list with values of 0 or 1 - convert to binary

The important thing to know here is about the doubling and adding the value of the current node.


# Partition list based on a given value

All values smaller than the given value should be on the left of the linked list.

All values greater than or equal should come on the right side.


# Reverse between

This problem is super challenging

```python
current_node = prev.next

for i in range(right - left):
    node_to_move = curr.next
    curr.next = node_to_move.next
    node_to_move.next = prev.next
    prev.next = node_to_move
```