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

    def append(self, value):
        # Edge case when the linked list has no nodes
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
        # Edge case with no nodes
        if not self.head:
            return None
        
        popped_node = self.tail

        # Edge case with only 1 node
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp

        self.length -= 1
        return popped_node.value
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        # Edge case with no nodes
        if not self.head:
            return None
        
        popped_node = self.head
        
        # Edge case with only 1 node
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1
        return popped_node.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp
    
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.get(index)
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        new_node = Node(value)
        
        # If index = 0
        if index == 0:
            return self.prepend(value)
        
        # If last index
        if index == self.length:
            return self.append(value)

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        removed_node = pre.next
        pre.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        return removed_node.value
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    
    def find_middle_node(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow