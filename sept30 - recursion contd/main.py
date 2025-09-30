class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Starting the binary search tree from the root node of value
class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    # Contains method
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    # Insert method
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        else:
            # Case 1 - leaf node
            if current_node.left == None and current_node.right == None:
                return None
            
            # Case 2 - only right node
            elif current_node.left == None:
                current_node = current_node.right

            # Case 3 - only left node
            elif current_node.right == None:
                current_node = current_node.left

            # Case 4 - both node and right subtree
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        
        return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
