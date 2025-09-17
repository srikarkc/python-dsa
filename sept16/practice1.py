class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail = new_node, new_node
        self.length = 1

    # Method 1 - append
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    # Method 2 - pop and return the removed node
    def pop(self):
        if not self.head:
            return None
        
        popped_node = self.tail
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        
        self.length -= 1
        return popped_node
    
    # Method 3 - Prepend
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    # Method 4 - Pop first
    def pop_first(self):
        if not self.head:
            return
        
        popped_node = self.head
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    # Method 5 - Get
    def get(self, index):
        if not self.head or (index < 0 or index >= self.length):
            return None
        
        temp = self.head
        if index <= (self.length // 2):
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    # Method 6 - Set
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
        
    # Method 7 - Insert
    def insert(self, index, value):
        if not self.head or (index < 0 or index > self.length):
            return True
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.next = after
        new_node.prev = before

        before.next = new_node
        after.prev = new_node
        self.length += 1

        return True
    
    # Method 8 - Remove
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        
        popped_node = self.get(index)
        before = popped_node.prev
        after = popped_node.next

        before.next = after
        after.prev = before

        popped_node.next, popped_node.prev = None, None
        self.length -= 1
        return True