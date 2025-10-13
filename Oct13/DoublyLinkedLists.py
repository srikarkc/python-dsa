class Node:
    def __init__(self, value):
        self.value = value
        self.next, self.prev = None, None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = value
        self.head, self.tail = new_node, new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return
        popped_node = self.tail
        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return
        
        popped_node = self.head

        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < (self.length / 2):
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length - 1, index, -1):
                current = current.prev
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return True
    