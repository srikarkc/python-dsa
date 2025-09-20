# Trees

Binary tree - left and right node

A **full** tree - every node points to either zero or 2 nodes.

A **perfect** tree - every level is fully filled.

A **complete** tree - filled from left to right


## Binary Search Tree

All value greater than the current node value go to the right and the remaining to the left.

Insert is faster for a linked list but lookup() and remove() are faster for a binary search tree.

## Constructor

You can have a constructor point to a node initially or just to None. 

### Insert into a binary search tree

First of all, when you are inserting into a binary search tree. If the value is < then, go left or if the value is > then, go right. 

Next, you will need to see if there's a value there already; if not - then add this into that spot. If there is a node there already; then, compare above condition again. 

This leads us to conclude that we will need a while loop. 

One edge case is if the root node is pointing to None --> Then, we can set the root node to point to the new node. 

We will need a pointer along all of these operations so we use a temp variable.

We also have another edge condition when the current node is equal to one of the nodes in the tree already. 

We cannot have duplicates in a tree so return False if that happens.