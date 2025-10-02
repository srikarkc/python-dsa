# 1 - Sorted Stack problem


# 2 - Queue using stacks

(common interview question - not ideal)

Enque using stacks.

---

# Trees

A linkedlist is a form of tree. It's just one that doesn't fork.

Binary tree - left and right node

A **full** tree - every node points to either zero or 2 nodes.

A **perfect** tree - every level is fully filled.

A **complete** tree - filled from left to right

Number of nodes in each level = 2 ^ (number of levels) - 1

O(log n) for searching in the tree / adding / removing to the binary search tree.

Worst case of a binary search tree is if nodes are only on the right - this will cause O(n).

If adding to the data structure is important (i.e. bursts of data coming in) but the retrieval speed is not very important - then, the appropriate data structure would be a linked list.

Lookup and remove are better for binary search tree.