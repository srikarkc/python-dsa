# Linked Lists

Lists are stored in contiguous areas of memory while linked lists are not.

Each node only have information about its value and a pointer to the next node.

## Big O

1. Adding to the end - O(1)
2. Removing from the end - O(n)
3. Adding to the front - O(1)
4. Removing from the front - O(1)
5. Inserting into the middle - O(n)
6. Removing from the middle - O(n)
7. Finding by index/value - O(n)

In comparison to Lists:
1. For lists - pop is O(1) while linked list - pop is O(n)
2. For lists - Lookup by index is O(1) while linked list is O(n)
3. Prepend & Pop first is better for linked list O(1) while O(n) for lists