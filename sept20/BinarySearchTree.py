class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

# Binary search tree which initializes to a value
class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

# Binary search tree which initializes to None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root

        # while new_node has not been added into the tree
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
            # If the node value exists already
            else:
                return False
            
    def contains(self, value):
        
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:  # value == temp.value
                return True
        
        return False