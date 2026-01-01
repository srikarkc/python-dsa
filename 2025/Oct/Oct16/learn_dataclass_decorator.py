# What I have been doing so far
class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

# Better way of doing this
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None