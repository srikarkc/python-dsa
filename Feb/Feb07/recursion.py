def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def array_sum(arr):
    if not arr:
        return 0
    return arr[0] + array_sum(arr[1:])

# problem 1 - find the height of a binary tree
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left) + height(node.right))

# problem 2 - count the number of nodes
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
