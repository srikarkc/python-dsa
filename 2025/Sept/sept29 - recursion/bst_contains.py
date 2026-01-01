def __r_contains(self, current_node, value):
    if current_node == None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return __r_contains(current_node.left, value)
    if value > current_node.value:
        return __r_contains(current_node.right, value)
    
def r_contains(self, value):
    return __r_contains(self.root, value)