class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # Method 1 - print stack
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    # Method 2 - Push onto stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    # Method 3 - Pop from stack
    def pop(self):
        if not self.top:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.height -= 1
        return popped_node
    

    
# my_stack = Stack(1)
# my_stack.push(2)
# my_stack.print_stack()
# my_stack.pop()
# print("---")
# my_stack.print_stack()