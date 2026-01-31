class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class Solution:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    # remove a node
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # add a node to the head
    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        self.head.next.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._insert(node)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]