def height(node):
    if node is None:
        return -1
    height_l = height(node.left)
    height_r = height(node.right)
    return 1 + max(height_l, height_r)
