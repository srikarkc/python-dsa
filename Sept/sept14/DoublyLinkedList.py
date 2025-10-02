class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node = Node(value)

        # Edge case when the doubly linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):

        # Edge case when the doubly linked list is empty
        if self.head is None:
            return None
        # Edge case with only 1 node
        elif self.head is self.tail:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None

        self.length -= 1
        return popped_node.value
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head, self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):

        if not self.head:
            return None
        
        # Edge case with only 1 node
        popped_node = self.head
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.head.prev = None
            
        self.length -= 1
        return popped_node.value
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp
    
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
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next

            before.next = new_node
            after.prev = new_node

            new_node.prev = before
            new_node.after = after

            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        # remove from the middle
        node = self.get(index)       # node to remove
        prev_node = node.prev
        next_node = node.next

        # relink neighbors
        prev_node.next = next_node
        next_node.prev = prev_node

        # fully detach node
        node.prev = None
        node.next = None

        self.length -= 1
        return node.value
    
    def check_palindrome(self):
        first = self.head
        last = self.tail

        for i in range(self.length // 2):
            if first.value != last.value:
                return False
            first = first.next
            last = last.prev

        return True
