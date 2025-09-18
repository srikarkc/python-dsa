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
        while temp:
            print(temp.value)
            temp = temp.nexft

    # Method 1 - Enqueue
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first, self.last = new_node, new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    # Method 2 - Dequeue
    def dequeue(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node