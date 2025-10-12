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
        current = self.head
        while current:
            print(current.value)
            current = current.next


    def append(self, value):
        new_node = Node(value)
        current = self.head
        if not current:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # The problem with this solution is that it does not check for an empty linked list at the end and set head/tail to None as req'd
    def pop(self):
        if not self.head:
            return None
        
        popped_node = self.tail

        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1

        return popped_node.value
    
    def pop_solution_from_course(self):
        if self.length == 0:
            return None
        
        temp, pre = self.head, self.head

        while temp.next:
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
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def pop_first(self):
        if self.length == 0:
            return None
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None

        self.length -= 1

        if self.length == 0:
            self.tail = None

        return popped_node
    

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        
        return current.value
    

    def set(self, index, value):
        node_to_change = self.get(index)
        if node_to_change:
            node_to_change.value = value
            return True
        return False
    

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        new_node = Node(value)
        temp = self.head
        pre = self.get(index - 1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.pop_first()
        elif index == (self.length - 1):
            self.pop()
        pre = self.get(index - 1)
        popped_node = pre.next
        pre.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return True
    

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


    # Problems
    def find_middle_node(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    
    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

def find_kth_node_from_end(self, ll, k):
    slow = ll.head
    fast = ll.head
    
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next
        
    while fast is not None:
        slow = slow.next
        fast = fast.next
        
    return slow