from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        temp = self.root

        if temp is None:
            self.root = new_node
            return True
        
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                return False
            
    def contains(self, value):
        temp = self.root

        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        
        return False