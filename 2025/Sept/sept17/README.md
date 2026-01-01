# Stack and Queues babbyy

Push things on top of stack or off of stack.

We can use a LinkedList to represent a stack.

We can have a top pointer which is similar to the head pointer.

The terminated end pointing to None should be at the end.

---

Queues are first in first off.

In a queue, you add on one end and remove from the other end.

If you use a list - you will have O(n) when you add or remove from the front of the queue.

If you use a singly linked list - you will have O(n) only when removing from the end of the list.

The rest of the operations - adding/removing from the start and adding to the last are O(1).

Ensure, you never remove from the last of the queue.

head pointer is the **first** and tail pointer is the **last**.

