class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""

    for char in input_string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

def is_balanced_parentheses(input_str):
    my_stack = Stack()
    for i in input_str:
        if i == "(":
            my_stack.push(i)
        elif i == ")":
            if my_stack.peek() == "(":
                my_stack.pop()
            else:
                return False
        else:
            print("Invalid input")
    if my_stack.is_empty():
        return True
    else:
        return False