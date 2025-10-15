class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first, self.last = new_node, new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first, self.length = new_node, new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return
        
        popped_value = self.first
        if self.length == 1:
            self.first, self.last = None, None
        else:
            self.first = self.first.next
            popped_value.next = None
        
        self.length -= 1
        return popped_value