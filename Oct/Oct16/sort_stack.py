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

def sort_stack(s1: Stack):
    s2 = Stack()

    while not s1.is_empty():
        temp = s1.pop()
        while not s2.is_empty() and s2.peek() > temp:
            s1.push(s2.pop())
        
        s2.push(temp)
    
    while not s2.is_empty():
        s1.push(s2.pop())