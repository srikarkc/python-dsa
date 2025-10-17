from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, Generator, Any

@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

class BST:
    def __init__(self, items: Iterable[int] = ()):
        self.root: Optional[Node] = None
        for x in items:
            self.insert(x)

    def search(self, key: int) -> None:
        cur = self.root
        while cur:
            if key == cur.key: return True
            cur = cur.left if key < cur.key else cur.right
        return False
    
    def insert(self, key: int) -> None:
        if not self.root:
            self.root = Node(key)
            return
        curr = self.root
        parent = None
        while curr:
            parent = curr
            if key == curr.key:
                return
            curr = curr.left if curr < curr.key else curr.right
        if key < parent.key:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

    