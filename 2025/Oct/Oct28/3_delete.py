def __delete_node(self, current_node, value):
    if current_node == None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    if value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    return current_node


def delete_node(self, value):
    self.__delete_node(self.root, value)