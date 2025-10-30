class Node:
    def __init__(self, value):
        self.value = value

def __delete_node(self, current_node, value):
    if current_node == None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    if value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    else:
        # Verify that the current node is leaf node
        if current_node.left == None and current_node.right == None:
            return None
        # if there's a value only on the right
        elif current_node.left == None:
            current_node = current_node.right
        # if there's a value only on the left
        elif current_node.right == None:
            current_node = current_node.left
        # if there is a value both on the left and the right
        else:
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)

    return current_node

# helper method to find the minimum value
def min_value(self, current_node):
    while current_node.left:
        current_node = current_node.left
    return current_node.value

def delete_node(self, value):
    # self.__delete_node(self.root, value) -- This way will not work when deleting the root node
    self.root = self.__delete_node(self.root, value)