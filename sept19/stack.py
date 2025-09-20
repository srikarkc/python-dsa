class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.height = 1

# Some methods have been omitted

def sorted_stack(input_stack):
    sorted_stack = Stack()

    while not input_stack.is_empty():
        temp = input_stack.peek()

        while sorted_stack.is_empty() or sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())

        sorted_stack.push(temp)

    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())