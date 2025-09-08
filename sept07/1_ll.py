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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # Edge case if the linked list is empty
        if self.head is None:
            return None
        
        # Edge case if only 1 node
        if self.head is self.tail:
            popped_value = self.head
            self.head = None
            self.tail = None
            self.tail -= 1
            return popped_value
        
        # Traverse to second-last node
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next

        popped_value = self.tail.value
        temp.next = None
        self.tail = temp
        self.length -= 1
        return popped_value
    
    def prepend(self, value):
        new_node = Node(value)
        # Edge case if the linked list is empty
        if self.head is None:  # or self.length == 0
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        # All other cases
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        # Edge case if linked list is empty
        if self.head is None:
            return None
        
        # Another edge case if only 1 item in the linked list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        
        temp = self.head
        popped_item = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return popped_item
    
    def get(self, index):
        # Edge case if index is out of bounds of the linked list
        if index < 0 or index >= self.length:
            print("Index out of bounds")
            return None

        output_node = self.head
        for i in range(index):
            output_node = output_node.next
        return output_node
    
    def set(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        pre = self.head
        for i in range(index - 1):
            pre = pre.next
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
        