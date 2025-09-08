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
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        # Edge case when no nodes
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self, value):
        # Edge case when ll is empty
        if self.head is None:
            return None
        popped_value = self.tail
        # Edge case when only 1 node
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_value
        # Iterate through to n-1 value
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        popped_value = self.tail
        temp.next = None
        self.tail = temp
        self.length -= 1
        return popped_value
    
    def prepend(self, value):
        new_node = Node(value)

        # Edge case linked list with no nodes
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
        
    def pop_first(self):
        # Edge case ll is empty
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.lenght == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        # Check if index is out of bounds
        if index < 0 or index >= self.length:
            print("Index out of bounds!")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(value)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)

        # Edge case when the list is empty
        if index == 0 and self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        
        # Check if index out of bounds
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return None
        
        # Insert at head
        if index == 0:
            self.prepend(value)

        if index == self.length:
            self.append(value)
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        # bounds check
        if index < 0 or index >= self.length:
            return None

        # remove head
        if index == 0:
            return self.pop_first()

        # remove tail
        if index == self.length - 1:
            return self.pop()

        # remove from middle
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        # prev = self.get(index - 1)  # We can use this line instead of the above
        removed = prev.next
        prev.next = removed.next
        removed.next = None
        self.length -= 1
        return removed
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after