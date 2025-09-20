class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        return self.stack1[-1]
    
    def is_empty(self):
        return len(self.stack1) == 0
    
    # This is the enqueue method

    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())