# Find middle node

The linked list does not have a length attribute. 

In case of even number of nodes; we return the first node from the second half.

`while fast is not None and fast.next is not None`

The first half of the above line is for even cases.


# Has Loop

Use the slow and fast pointer.

If pointers are never equal to each other - return False i.e. no Loop.

If pointers are equal at some point - there must be a loop.


# Remove duplicates

If you use `while slow.next is not None` instead of `while slow is not None` for the outer loop in O(n^2) solution; the last node will never be checked!