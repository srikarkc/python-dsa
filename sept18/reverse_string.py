class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
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
        return self.stack_list.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def reverse_string(input_str):
    my_stack = Stack()
    for i in input_str:
        my_stack.push(i)
    my_output_str = ""
    while not my_stack.is_empty():
        my_output_str += my_stack.pop()
    return my_output_str

# print(reverse_string("hello"))

# Problem 2
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
            print("Not a valid input to this method!")

    if my_stack.is_empty():
        return True
    else:
        return False
    
# Problem 3 - Sort stack
