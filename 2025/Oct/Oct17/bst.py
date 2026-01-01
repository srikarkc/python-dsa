class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        
        temp = self.root
        new_node = Node(value)
        
        if temp is None:
            self.root = new_node
            return True
        
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            # The following condition should mean that an exact node exists already
            else:
                return False

    def contains(self, value):
        temp = self.root
        
        while temp is not None:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        
        return False