class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if current_node.value == value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)

    # helper function
    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.left:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.right:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # Case 1 - only leaf node
            if current_node.left == None and current_node.right == None:
                return None
            
            # Case 2 - only left node or right node
            elif current_node.right == None:
                current_node = current_node.left
            elif current_node.left == None:
                current_node = current_node.right

            # Case 3 - we have a sub-tree
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right = self.__delete_node(current_node.right, subtree_min)
        
        return current_node
    
    # Code from here is for the BFS
    def BFS(self):
        current_node = self.root
        queue, results = [], []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return results
    
    def DFS_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)

    def DFS_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)

    def DFS_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)