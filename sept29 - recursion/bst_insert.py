class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# class BinarySearchTree:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.root = new_node

# We can start root from None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    # Notice in the recursive insert there is no return method
    def r_insert(self, value):
        self.__r_insert(self.root, value)