# Revision

## Understanding recursion

There's always a base case + recursive case.

The simplest example is the factorial problem

`factorial(n) = n * (n -1) * (n - 2) * .. * 1`

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

Every recursive call is pushed onto the call stack.

Another problem to think of is the sum of an array

```python
def array_sum(arr):
    # base case
    if not arr:
        return 0

    # recursive case
    first_num = arr[0]
    rest_of_nums = arr[1:]

    return first_num + array_sum(rest_of_nums)
```

Ask yourself 3 questions with recursion type problems:

1. What is the smallest possible input? -> base case
2. How do I reduce the problem size?
3. What do I do with the returned value?

## Trees

A tree is a data structure made up of nodes connected by edges with one rule:

Every node can have children, but only one parent (except the root).

Think family tree, not graph.

### DFS

Dfs is used for height, paths, & validity checks.

### BFS

Bfs is used for level order traversal, shortest path, right side view
