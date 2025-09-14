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
    
    def has_loop(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
            
        return False
    
    def find_kth_from_end(self, k):
        slow, fast = self.head, self.head

        for _ in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow
    

    # Problem 4 - remove duplicates
    def remove_duplicates(self):
        seen_values = set()

        prev = None
        curr = self.head

        while curr is not None:
            if curr.value in seen_values:
                prev.next = curr.next
                if curr is self.tail:
                    self.tail = prev
                nxt = curr.next
                curr.next = None
                self.lenght -= 1
                self.curr = nxt
            else:
                seen_values.add(curr.value)
                curr = curr.next
                prev = prev.next

    # Problem 5 - Binary to decimal
    def binary_to_decimal(self):
        if not self.head:
            return
        
        decimal = 0
        temp = self.head
        
        while temp is not None:
            decimal = (2 * decimal) + (temp.value)
            temp = temp.next

        return decimal
    
    # Problem 6 - Partition list based on a give value
    def partition_list(self, value):
        dummy1, dummy2 = Node(0), Node(0)
        p1, p2 = dummy1, dummy2

        temp = self.head

        while temp is not None:
            if temp.value < value:
                p1.next = temp
                p1 = p1.next
            elif temp.value >= value:
                p2.next = temp
                p2 = p2.next
            temp = temp.next

        p1.next = dummy2.next
        p2.next = None
        self.head = dummy1.next

        # reset tail
        self.tail = p1 if dummy2.next is None else p2

    def reverse_between(self,left,right):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        pre = dummy

        for i in range(left):
            pre = pre.next

        curr = pre.next

        for i in range(right - left):
            node_to_move = curr.next
            curr.next = node_to_move.next
            node_to_move.next = pre.next
            pre.next = node_to_move

        self.head = dummy.next

    # Problem 8 - swap pairs
    def swap_pairs(self):
        if not self.head or not self.head.next:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to the next pair
            prev = first

        self.head = dummy.next