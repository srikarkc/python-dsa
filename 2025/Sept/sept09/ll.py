class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # Edge case when ll is empty
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # Edge case when ll is empty
        if self.head is None:
            return None
        
        pre = self.head
        temp = self.head

        while (temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        # Edge case when the ll is empty
        if self.head is None or self.head is self.tail:
            self.append(value)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self, value):
        if self.head is None or self.head is self.tail:
            self.pop(value)
        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.length -= 1
        return popped.value
    
    def get(self, index):
        # Check if index is out of bounds
        if index < 0 or index >= self.length:
            print("Index out of bounds!")
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        # Check index out of bounds
        if index < 0 or index >= self.length:
            print("Index out of bounds!")
            return False
        temp = self.get(index)
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Index out of bounds")
            return False
        new_node = Node(value)
        temp = self.get(index)
