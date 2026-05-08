# 🌳 Trees — Interview Prep Handbook
### Target: LC 75 Trees | SWE / DevOps / SRE Interviews

> **How to use this guide:** Read top-to-bottom once to build the mental model.  
> Then use it as a reference when grinding problems.  
> Every pattern has a copy-paste Python template — memorize those.

---

## TABLE OF CONTENTS

1. [The Mental Model — Trees in One Page](#1-the-mental-model)
2. [Terminology and Tree Types](#2-terminology-and-tree-types)
3. [Recursive Thinking — Building the Intuition](#3-recursive-thinking)
4. [DFS vs BFS — When to Use What](#4-dfs-vs-bfs)
5. [Traversal Patterns — All 5 You Need](#5-traversal-patterns)
6. [Iterative Traversals Using Stacks & Queues](#6-iterative-traversals)
7. [Height, Balance, and Diameter](#7-height-balance-diameter)
8. [Path Sum Patterns](#8-path-sum-patterns)
9. [Lowest Common Ancestor (LCA)](#9-lowest-common-ancestor)
10. [BST Invariants and Tricks](#10-bst-invariants-and-tricks)
11. [Tree Construction Techniques](#11-tree-construction-techniques)
12. [Backtracking on Trees](#12-backtracking-on-trees)
13. [Serialization and Deserialization](#13-serialization-and-deserialization)
14. [Complexity Cheat Sheet](#14-complexity-cheat-sheet)
15. [Common Beginner Mistakes](#15-common-beginner-mistakes)
16. [Python Templates to Memorize](#16-python-templates-to-memorize)
17. [LC 75 Trees — Categorized Roadmap](#17-lc-75-trees-roadmap)

---

## 1. THE MENTAL MODEL

Before anything else, burn this into your brain:

```
A tree problem = the same subproblem applied to left and right subtrees,
                 combined in some way at the current node.
```

That's it. Every tree problem you'll ever face is a variation of this.

```
          1          ← Root (you start here)
        /   \
       2     3       ← Each child is the ROOT of its own subtree
      / \   / \
     4   5 6   7     ← Leaves: no children

Think of node 2: it's a mini-tree with root=2, left=4, right=5
Think of node 3: it's a mini-tree with root=3, left=6, right=7
```

**The recursive leap of faith:** When you're at node `1`, you don't worry
about what happens inside node `2`'s subtree. You just TRUST that your
function, when called on `2`, returns the correct answer for that subtree.
Then you combine those answers at node `1`.

This is the hardest mindset shift. Most beginners try to trace every recursive
call. Don't. Write the logic at ONE node, trust the recursion.

---

## 2. TERMINOLOGY AND TREE TYPES

### Core Vocabulary

```
Node:         The fundamental unit. Has a value + pointers to children.
Root:         Top node. Has no parent.
Leaf:         Node with NO children.
Edge:         The connection between parent and child.
Height:       Max edges from node down to deepest leaf.
              (leaf height = 0, null height = -1)
Depth:        Edges from root DOWN to this node. (root depth = 0)
Level:        Nodes at the same depth. Level 0 = root.
Subtree:      A node + all its descendants.
Ancestor:     Any node on the path from root to this node.
Descendant:   Any node reachable going DOWN from this node.

        root (depth=0, height=2)
        /      \
    depth=1   depth=1
    height=1  height=0(leaf)
    /    \
depth=2  depth=2
(leaf)   (leaf)
```

### Tree Types — Know the Differences

```
┌─────────────────────────────────────────────────────────────┐
│  BINARY TREE         BINARY SEARCH TREE (BST)               │
│                                                             │
│  Each node has       BST Property:                          │
│  at most 2 children  left < node < right (for ALL nodes)    │
│  (left, right)                                              │
│                           8                                 │
│       1                  / \                                │
│      / \                3   10                              │
│     2   3              / \    \                             │
│    /                  1   6    14                           │
│   4                      / \   /                            │
│                          4   7 13                           │
│                                                             │
│  No ordering rule    In-order traversal → sorted array!     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  COMPLETE BINARY TREE      PERFECT BINARY TREE              │
│                                                             │
│  All levels filled,        ALL levels fully filled.         │
│  last level filled         n = 2^h - 1 nodes                │
│  left to right.                                             │
│                                  1                          │
│       1                        /   \                        │
│      / \                      2     3                       │
│     2   3                    / \   / \                      │
│    / \  /                   4   5 6   7                     │
│   4   5 6                                                   │
│                                                             │
│  Heap is a complete BT     2^h - 1 nodes total              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  BALANCED BINARY TREE      DEGENERATE / SKEWED TREE         │
│                                                             │
│  Height = O(log n)         Height = O(n) ← worst case!      │
│  |height(left) -           Looks like a linked list         │
│   height(right)| <= 1                                       │
│  (AVL definition)              1                            │
│                                 \                           │
│       1                          2                          │
│      / \                          \                         │
│     2   3                          3                        │
│    /\   /\                          \                       │
│   4  5 6  7                          4                      │
└─────────────────────────────────────────────────────────────┘
```

### Heaps (for context — not in LC 75 Trees, but good to know)

```
Min-Heap: Parent ≤ children. Root = smallest element.
Max-Heap: Parent ≥ children. Root = largest element.

Stored as ARRAY (not pointer-based):
  parent(i) = (i-1) // 2
  left(i)   = 2*i + 1
  right(i)  = 2*i + 2

In Python: import heapq  # min-heap by default
```

### Tries (Prefix Trees — appears in LC 75!)

```
A Trie stores strings character by character.
Each node = one character.

Words: ["apple", "app", "apt"]

        root
        |
        a
        |
        p
       / \
      p   t
      |   |
      l   (end)
      |
      e
      |
    (end)

Use cases: autocomplete, prefix search, spell check
```

---

## 3. RECURSIVE THINKING — BUILDING THE INTUITION

### The 3-Step Recursive Framework

For EVERY tree problem, ask these three questions:

```
STEP 1: BASE CASE
  → What happens when node is None?
  → What happens at a leaf?
  → Return value must make sense for the parent call.

STEP 2: RECURSIVE CALLS
  → Call the function on left subtree
  → Call the function on right subtree
  → TRUST that these return correct answers

STEP 3: COMBINE
  → How do you use left_result + right_result + current node's value
    to produce the answer for the CURRENT subtree?
```

### Worked Example: Find Height of Tree

**Problem:** Return the height of a binary tree. (Leaf = 0, null = -1)

```python
# STEP 1: Base case
# If node is None → height is -1 (no node, no edge)

# STEP 2: Recursive calls
# left_height  = height(node.left)
# right_height = height(node.right)

# STEP 3: Combine
# height of current node = 1 + max(left_height, right_height)
# (one edge to go down to the deeper child)

def height(node):
    if node is None:          # Base case
        return -1
    left_h  = height(node.left)   # Trust this
    right_h = height(node.right)  # Trust this
    return 1 + max(left_h, right_h)  # Combine
```

```
Trace on:    1
            / \
           2   3
          /
         4

height(4) → left=-1, right=-1 → 1+max(-1,-1) = 0  ✓ (leaf)
height(2) → left=0,  right=-1 → 1+max(0,-1)  = 1  ✓
height(3) → left=-1, right=-1 → 1+max(-1,-1) = 0  ✓
height(1) → left=1,  right=0  → 1+max(1,0)   = 2  ✓
```

### The Call Stack — Visualized

```
Calling height(1):
  ├── height(2) called
  │     ├── height(4) called
  │     │     ├── height(None) → -1
  │     │     └── height(None) → -1
  │     │   returns 0
  │     ├── height(None) → -1
  │   returns 1
  ├── height(3) called
  │     ├── height(None) → -1
  │     └── height(None) → -1
  │   returns 0
  returns 2

STACK at deepest point (inside height(4), left child):
  [height(1), height(2), height(4), height(None)]
   ← bottom                                  top →
```

**Key insight:** The call stack mirrors the path from root to current node.
Space complexity of recursive DFS = O(h) where h = height of tree.

### Two Types of Recursive Problems

```
TYPE 1: BOTTOM-UP (Post-order style)
  → Compute answers in children first, then combine at parent.
  → Use when: height, diameter, path sums, any "bubble up" problem.
  → left = recurse(left); right = recurse(right); return combine(left, right)

TYPE 2: TOP-DOWN (Pre-order style)
  → Pass information DOWN to children via parameters.
  → Use when: path sums from root, tracking running sum, validating BST.
  → process(node); recurse(left, extra_info); recurse(right, extra_info)
```

---

## 4. DFS VS BFS — WHEN TO USE WHAT

### Decision Framework

```
┌──────────────────────────────────────────────────────────────┐
│                    TREE PROBLEM                              │
│                       │                                      │
│         ┌─────────────┴─────────────┐                       │
│         ▼                           ▼                        │
│    "Level-by-level"           "Path / depth"                 │
│    "Shortest path"            "Root to leaf"                 │
│    "Minimum depth"            "Subtree property"             │
│    "Connect same-level"       "Height/balance"               │
│    "Zigzag traversal"         "Ancestors"                    │
│         │                           │                        │
│        BFS                         DFS                       │
│    (queue-based)           (stack or recursion)              │
└──────────────────────────────────────────────────────────────┘
```

### BFS Mental Model — "Ripples in a pond"

```
Process all nodes at distance 1, then distance 2, then distance 3...

          1          ← Process level 0 first
        /   \
       2     3       ← Then level 1
      / \   / \
     4   5 6   7     ← Then level 2

Order: 1 → 2,3 → 4,5,6,7
Tool:  deque (queue) — FIFO
```

### DFS Mental Model — "Go deep before going wide"

```
Explore as far as possible down one branch before backtracking.

          1
        /   \
       2     3
      / \
     4   5

Pre-order DFS: 1 → 2 → 4 → 5 → 3
Tool: recursion (implicit stack) or explicit stack — LIFO
```

---

## 5. TRAVERSAL PATTERNS — ALL 5 YOU NEED

### The Big 3: Pre / In / Post Order

**Memory trick: where do you process the ROOT?**

```
PRE-order:   ROOT → Left → Right   (Root is FIRST)
IN-order:    Left → ROOT → Right   (Root is in the MIDDLE)
POST-order:  Left → Right → ROOT   (Root is LAST / at POST-end)

        1
       / \
      2   3
     / \
    4   5

PRE-order:  [1, 2, 4, 5, 3]    ← Good for: copy tree, serialize, prefix
IN-order:   [4, 2, 5, 1, 3]    ← Good for: BST → sorted array, validate BST
POST-order: [4, 5, 2, 3, 1]    ← Good for: delete tree, bottom-up aggregation
```

### Visualizing with L-R-Root labels

```
For each node, mark when it's visited:

Pre:  Visit node BEFORE going left or right
       1*               Visit 1
      / \
     2*  3              Visit 2
    / \
   4*  5*               Visit 4, then 5
        \
         3*             Visit 3
Result: 1,2,4,5,3

In:   Visit node BETWEEN left and right
       1                (1 waits)
      / \
     2   3              (2 waits)
    / \
   4*  5*               Visit 4, backtrack → visit 2, visit 5
        
   → 4, backtrack → 2, → 5, backtrack → 1, → 3
Result: 4,2,5,1,3
```

### Recursive Templates

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# PRE-ORDER
def preorder(node):
    if not node:
        return
    print(node.val)        # ← Process ROOT first
    preorder(node.left)
    preorder(node.right)

# IN-ORDER
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)        # ← Process ROOT in middle
    inorder(node.right)

# POST-ORDER
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)        # ← Process ROOT last
```

### Level-Order Traversal (BFS)

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue  = deque([root])
    
    while queue:
        level_size = len(queue)      # ← CRITICAL: snapshot size before processing
        level = []
        
        for _ in range(level_size):  # Process exactly this many nodes
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)         # One list per level
    
    return result

# Output for tree above: [[1], [2,3], [4,5,6,7]]
```

**Why `level_size = len(queue)` matters:**

```
Before processing level 1:  queue = [2, 3]  → level_size = 2
We process exactly 2 nodes, adding their children to the queue.
After the inner loop:       queue = [4, 5, 6, 7]  → next level ready.

Without this snapshot, you'd mix levels together.
```

### Reverse Level-Order and Zigzag

```python
# REVERSE level order → just reverse the result list
result[::-1]

# ZIGZAG (alternate left-right, right-left per level)
def zigzag_level_order(root):
    if not root:
        return []
    result = []
    queue  = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        
        if not left_to_right:
            level.reverse()              # ← Only difference!
        result.append(level)
        left_to_right = not left_to_right
    
    return result
```

---

## 6. ITERATIVE TRAVERSALS USING STACKS & QUEUES

Interviewers sometimes ask: "Can you do it iteratively?"

### Iterative Pre-Order (Stack)

```
KEY INSIGHT: Stack is LIFO. Push RIGHT first, then LEFT.
That way LEFT is popped (processed) first → Root, Left, Right order.

Stack state for tree [1, 2, 3, 4, 5]:
Push 1        → stack: [1]
Pop 1, visit  → push 3, push 2  → stack: [3, 2]
Pop 2, visit  → push 5, push 4  → stack: [3, 5, 4]
Pop 4, visit  → no children    → stack: [3, 5]
Pop 5, visit  → no children    → stack: [3]
Pop 3, visit  → no children    → stack: []
Result: 1, 2, 4, 5, 3  ✓
```

```python
def preorder_iterative(root):
    if not root:
        return []
    result = []
    stack  = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)  # Push right FIRST
        if node.left:  stack.append(node.left)   # Left popped first
    
    return result
```

### Iterative In-Order (Stack)

```
Trickier — need to go as far LEFT as possible first.

Pattern: "go left until you can't, then process, then go right"

        4
       / \
      2   5
     / \
    1   3

Go left: push 4, push 2, push 1
Pop 1: visit 1, no right child
Pop 2: visit 2, go right → push 3
Pop 3: visit 3, no right
Pop 4: visit 4, go right → push 5
Pop 5: visit 5
Result: 1, 2, 3, 4, 5  ✓
```

```python
def inorder_iterative(root):
    result = []
    stack  = []
    curr   = root
    
    while curr or stack:
        # Go as far LEFT as possible
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # Process node
        curr = stack.pop()
        result.append(curr.val)
        
        # Now explore RIGHT subtree
        curr = curr.right
    
    return result
```

### Iterative Post-Order (Two-Stack trick)

```
Trick: Post-order is reverse of (Root, Right, Left).
So do pre-order but push LEFT before RIGHT, then reverse result.

Pre-order (left first):  Root → Right → Left
Reverse:                 Left → Right → Root  = Post-order ✓
```

```python
def postorder_iterative(root):
    if not root:
        return []
    result = []
    stack  = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:  stack.append(node.left)   # Push left FIRST
        if node.right: stack.append(node.right)  # Right popped first
    
    return result[::-1]   # Reverse at the end
```

---

## 7. HEIGHT, BALANCE, AND DIAMETER

### Height (Recursive — Bottom-Up)

```python
def height(node):
    if not node:
        return -1    # null node has height -1
    return 1 + max(height(node.left), height(node.right))

# Some problems use 0 for null → then leaf = 1
# Convention depends on problem. Read carefully.
```

### Checking if a Tree is Balanced (LC 110)

```
A tree is balanced if EVERY node's left and right subtrees
differ in height by AT MOST 1.

Naive: O(n²) — compute height at every node separately.
Better: O(n) — compute height and check balance in ONE pass.

Key idea: return -1 as a "poison" value meaning "already unbalanced".
```

```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0              # height of null = 0 (using 0-based here)
        
        left  = check(node.left)
        right = check(node.right)
        
        # If any subtree returned -1, propagate the poison
        if left == -1 or right == -1:
            return -1
        
        # Check balance at this node
        if abs(left - right) > 1:
            return -1             # Unbalanced → return poison
        
        return 1 + max(left, right)   # Return actual height
    
    return check(root) != -1

# Pattern: "early termination via sentinel value (-1)"
# This is extremely common in tree problems!
```

### Diameter of Binary Tree (LC 543)

```
Diameter = longest path between ANY two nodes (may not pass through root).

The path through a node = left_height + right_height
                          (edges going left + edges going right)

        1
       / \
      2   3
     / \
    4   5

Diameter through node 2: height(4) + height(5) = 0 + 0 = 1? 
Wait — diameter counts EDGES. Path 4→2→5 = 2 edges.

For each node: path_through_node = left_height + right_height
where height here means number of EDGES to deepest leaf.
If null → height = 0 (no edges below)
If leaf → height = 0 (no edges below)

Actually: left_depth + right_depth where depth of null = 0
```

```python
def diameter_of_binary_tree(root):
    self_diameter = [0]   # Use list to allow mutation inside nested function
    
    def depth(node):
        if not node:
            return 0
        
        left_d  = depth(node.left)
        right_d = depth(node.right)
        
        # Update global max diameter
        self_diameter[0] = max(self_diameter[0], left_d + right_d)
        
        # Return depth of this subtree
        return 1 + max(left_d, right_d)
    
    depth(root)
    return self_diameter[0]

# PATTERN: "global max updated during recursion, but function returns something else"
# This pattern appears in: diameter, max path sum, longest path
```

```
Trace:
depth(4) = 1+max(0,0) = 1, diameter updated to max(0, 0+0)=0
depth(5) = 1+max(0,0) = 1, diameter updated to max(0, 0+0)=0
depth(2):
  left_d=1, right_d=1
  diameter = max(0, 1+1) = 2   ← This is the answer!
  returns 2
depth(3) = 1
depth(1):
  left_d=2, right_d=1
  diameter = max(2, 2+1) = 3?  
  
Wait — path through 1 = depth(2-subtree) + depth(3-subtree) = 2+1=3
But visually: 4→2→5 is length 2, and 4→2→1→3 is length 3.
So diameter IS 3 (longest path = 4→2→1→3). Correct!
```

---

## 8. PATH SUM PATTERNS

### Pattern 1: Root-to-Leaf Path Sum (LC 112)

```
Does any root-to-leaf path sum to target?

        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1

Target = 22. Path: 5→4→11→2 = 22 ✓
```

```python
def has_path_sum(root, target_sum):
    if not root:
        return False
    
    # At a leaf: check if remaining sum equals leaf value
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Pass remaining sum down
    remaining = target_sum - root.val
    return has_path_sum(root.left, remaining) or \
           has_path_sum(root.right, remaining)

# PATTERN: "subtract from target as you go down"
# Leaf condition: remaining == 0 (or root.val == remaining)
```

### Pattern 2: Path Sum — All Paths (LC 113)

```python
def path_sum(root, target_sum):
    result = []
    
    def dfs(node, remaining, path):
        if not node:
            return
        
        path.append(node.val)
        
        # Check leaf
        if not node.left and not node.right and remaining == node.val:
            result.append(list(path))   # list(path) = snapshot copy!
        
        dfs(node.left,  remaining - node.val, path)
        dfs(node.right, remaining - node.val, path)
        
        path.pop()   # ← BACKTRACK: undo before returning
    
    dfs(root, target_sum, [])
    return result

# PATTERN: "append → recurse → pop" = classic backtracking on trees
```

### Pattern 3: Max Path Sum (LC 124 — hard but important)

```
Path can go through ANY two nodes (not just root-to-leaf).
Can go left subtree → current node → right subtree.

KEY INSIGHT: When returning UP to parent, you can only pick ONE branch.
A "split" (using both children) can only happen at the current node.
```

```python
def max_path_sum(root):
    global_max = [float('-inf')]
    
    def max_gain(node):
        if not node:
            return 0
        
        # Only take positive contributions (ignore negative branches)
        left_gain  = max(max_gain(node.left),  0)
        right_gain = max(max_gain(node.right), 0)
        
        # Price of the path passing through this node (the "split" point)
        path_through = node.val + left_gain + right_gain
        global_max[0] = max(global_max[0], path_through)
        
        # Return max gain if continuing upward (pick ONE side)
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return global_max[0]

# PATTERN: 
# "What's the best I can offer my parent?" → return node.val + max(left, right)
# "What's the best path through ME?"       → node.val + left + right
# Update global answer with "path through me"
# Return only single-branch for parent
```

---

## 9. LOWEST COMMON ANCESTOR (LCA)

### The Core Insight

```
LCA(p, q) = the deepest node that has BOTH p and q as descendants
            (a node is a descendant of itself).

        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

LCA(5, 1) = 3   (3 is the root of both subtrees)
LCA(5, 4) = 5   (5 is an ancestor of 4, so LCA is 5)
LCA(6, 4) = 5   (5 is the split point)
```

### The Recursive Logic

```
At each node, ask: "Is p or q in my left subtree? My right subtree? Am I p or q?"

Case 1: Found p or q at current node → return current node
Case 2: p in left subtree, q in right subtree → current node is LCA
Case 3: Both in left subtree → LCA is in left subtree
Case 4: Both in right subtree → LCA is in right subtree
```

```python
def lowest_common_ancestor(root, p, q):
    # Base case: reached null, or found p or q
    if not root or root == p or root == q:
        return root
    
    left  = lowest_common_ancestor(root.left,  p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # Both sides returned something → current node is LCA
    if left and right:
        return root
    
    # Only one side found something → propagate upward
    return left if left else right

# Time: O(n), Space: O(h)
```

```
Trace for LCA(6, 4) in tree above:

LCA(3, 6, 4):
  left  = LCA(5, 6, 4)
    left  = LCA(6, 6, 4) → returns 6 (found p=6!)
    right = LCA(2, 6, 4)
      left  = LCA(7, 6, 4) → None
      right = LCA(4, 6, 4) → returns 4 (found q=4!)
      → left=None, right=4, both? No. return right=4
    → left=6, right=4, BOTH! → return node 5
  right = LCA(1, 6, 4) → None (6,4 not in right subtree)
  → left=5, right=None → return 5 ✓
```

### LCA in BST (Easier!)

```python
def lca_bst(root, p, q):
    # Both smaller → go left
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)
    # Both larger → go right
    if p.val > root.val and q.val > root.val:
        return lca_bst(root.right, p, q)
    # Split point → current node is LCA
    return root
```

---

## 10. BST INVARIANTS AND TRICKS

### The BST Property

```
For EVERY node n in a BST:
  ALL nodes in left subtree  < n.val
  ALL nodes in right subtree > n.val

Common mistake: only checking immediate children.
This BST is INVALID:

        10
       /  \
      5    15
     / \
    1   12      ← 12 > 10, violates 10's constraint!
```

### Validate BST (LC 98)

```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left,  min_val,   node.val) and
                validate(node.right, node.val,  max_val))
    
    return validate(root, float('-inf'), float('inf'))

# PATTERN: Pass min/max bounds down the tree.
# Left child must be < parent → max_val = parent.val
# Right child must be > parent → min_val = parent.val
```

### BST Search

```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)

# Time: O(h) = O(log n) for balanced BST, O(n) for skewed
```

### BST Insert

```python
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)   # Found the right spot!
    if val < root.val:
        root.left  = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root   # ← Return root so parent links are maintained
```

### Kth Smallest in BST (In-order = Sorted)

```python
def kth_smallest(root, k):
    # In-order traversal gives sorted order for BST
    stack = []
    curr  = root
    count = 0
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right
```

---

## 11. TREE CONSTRUCTION TECHNIQUES

### From Pre-order + In-order (LC 105)

```
Key insight:
  - pre-order[0]     = ROOT of current tree
  - In-order: find ROOT position → everything LEFT is left subtree,
              everything RIGHT is right subtree

Pre: [3, 9, 20, 15, 7]
In:  [9, 3, 15, 20, 7]

root = 3 (pre[0])
In-order: [9] | 3 | [15, 20, 7]
           ↑               ↑
        left subtree   right subtree (size=3)
Pre-order splits: [9] | [20, 15, 7]
                   ↑        ↑
               left pre  right pre
```

```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid  = inorder.index(preorder[0])   # Find root in inorder
    
    root.left  = build_tree(preorder[1 : mid+1],   inorder[:mid])
    root.right = build_tree(preorder[mid+1 :],     inorder[mid+1:])
    
    return root

# Optimize with hashmap for O(1) index lookup:
def build_tree_fast(preorder, inorder):
    idx_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = [0]   # Use list for mutation in nested scope
    
    def build(left, right):
        if left > right:
            return None
        root_val = preorder[pre_idx[0]]
        pre_idx[0] += 1
        root = TreeNode(root_val)
        mid  = idx_map[root_val]
        root.left  = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    
    return build(0, len(inorder) - 1)
```

### From Sorted Array → Balanced BST (LC 108)

```
To build a BALANCED BST from sorted array:
  → Always pick the MIDDLE element as root
  → Recursively do the same for left half and right half

[1, 2, 3, 4, 5, 6, 7]
     mid = 3 (index 3, value 4)
     
        4
       / \
  [1,2,3]  [5,6,7]
   mid=2      mid=6
     2           6
    / \         / \
   1   3       5   7
```

```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid  = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left  = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root
```

---

## 12. BACKTRACKING ON TREES

### The Backtracking Template

```
Backtracking = DFS with UNDO

When you go down a path, you ADD something to state.
When you come BACK UP, you REMOVE it (undo).

The key line: path.pop() after both recursive calls.
```

```python
def find_all_paths(root, target):
    result = []
    
    def dfs(node, path, remaining):
        if not node:
            return
        
        # Choose
        path.append(node.val)
        
        # Explore (at leaf with correct sum → record)
        if not node.left and not node.right and remaining == node.val:
            result.append(list(path))   # COPY the path, not reference!
        else:
            dfs(node.left,  path, remaining - node.val)
            dfs(node.right, path, remaining - node.val)
        
        # Unchoose (backtrack)
        path.pop()
    
    dfs(root, [], target)
    return result

# CRITICAL MISTAKE: result.append(path) ← BUG! path will be emptied later.
# ALWAYS: result.append(list(path)) ← makes a snapshot copy.
```

### Why `list(path)` Matters

```
path = [5, 4, 11, 2]
result.append(path)      # result[0] IS path (same object!)
path.pop()               # Now path = [5, 4, 11], result[0] also changed!

path = [5, 4, 11, 2]
result.append(list(path))  # result[0] is a NEW list with same values
path.pop()                 # path = [5, 4, 11], result[0] = [5, 4, 11, 2] ✓
```

---

## 13. SERIALIZATION AND DESERIALIZATION

### Concept

```
Serialize:   Convert tree → string (to store or transmit)
Deserialize: Convert string → tree (reconstruct)

A common approach: pre-order with null markers

        1
       / \
      2   3
         / \
        4   5

Serialized: "1,2,null,null,3,4,null,null,5,null,null"
```

```python
class Codec:
    def serialize(self, root):
        result = []
        
        def dfs(node):
            if not node:
                result.append('null')
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(result)
    
    def deserialize(self, data):
        vals = iter(data.split(','))  # Use iterator for O(1) advancement
        
        def build():
            val = next(vals)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left  = build()
            node.right = build()
            return node
        
        return build()

# WHY iter()? 
# Instead of tracking index manually, iter() advances automatically.
# next(vals) gets the next value and moves the pointer.
```

---

## 14. COMPLEXITY CHEAT SHEET

```
┌──────────────────────────────────────────────────────────────────┐
│ OPERATION           │ BALANCED BST  │ UNBALANCED    │ COMPLETE   │
├──────────────────────────────────────────────────────────────────┤
│ Search              │ O(log n)      │ O(n)          │ O(log n)   │
│ Insert              │ O(log n)      │ O(n)          │ O(log n)   │
│ Delete              │ O(log n)      │ O(n)          │ O(log n)   │
│ In-order traversal  │ O(n)          │ O(n)          │ O(n)       │
├──────────────────────────────────────────────────────────────────┤
│ SPACE (recursion)   │ O(log n)      │ O(n)          │ O(log n)   │
│  = O(height)        │ stack depth   │ worst case    │            │
├──────────────────────────────────────────────────────────────────┤
│ BFS (level-order)   │ O(n) time,   O(w) space where w = max width│
│                     │ worst case w = n/2 (last level, perfect BT)│
└──────────────────────────────────────────────────────────────────┘

SPACE COMPLEXITY RULES:
  Recursive DFS  → O(h) stack frames = O(log n) balanced, O(n) skewed
  Iterative DFS  → O(h) explicit stack
  BFS            → O(w) queue = O(n) in worst case (wide trees)
  Storing result → O(n) always (you have n values)
```

---

## 15. COMMON BEGINNER MISTAKES

### Mistake 1: Forgetting `if not root: return None` vs `return 0`

```python
# Wrong for functions that return a TreeNode:
def some_func(root):
    if not root:
        return 0    # Bug! Caller expects None or TreeNode
    ...

# Wrong for functions that count/compute:
def height(root):
    if not root:
        return None  # Bug! We need -1 or 0
    ...

# Rule: Match your base case return TYPE to what the function returns.
```

### Mistake 2: Modifying path without copying for results

```python
result.append(path)        # ❌ BUG: appends REFERENCE
result.append(list(path))  # ✅ appends a copy
result.append(path[:])     # ✅ also fine
```

### Mistake 3: Not handling single-node tree

```
Tree with just root (no left, no right).
Always test your solution mentally on: [], [1], [1, 2], [1, 2, 3].
```

### Mistake 4: BST validation with just parent check

```python
# ❌ WRONG: only checks immediate parent
def is_bst_wrong(node):
    if not node:
        return True
    if node.left and node.left.val >= node.val:
        return False
    if node.right and node.right.val <= node.val:
        return False
    return is_bst_wrong(node.left) and is_bst_wrong(node.right)

# This passes for the invalid tree shown in Section 10.
# ✅ CORRECT: pass min/max bounds (shown in Section 10).
```

### Mistake 5: Confusing height with depth

```
Height: measured from node DOWN to farthest leaf (bottom-up)
Depth:  measured from ROOT down to node (top-down)

Height of root = height of tree.
Depth of root  = 0.
```

### Mistake 6: Level-order without snapshotting queue size

```python
# ❌ WRONG: doesn't separate levels
while queue:
    node = queue.popleft()    # Processes all nodes mixed together
    ...

# ✅ CORRECT: snapshot level size
while queue:
    level_size = len(queue)   # Freeze the count for this level
    for _ in range(level_size):
        ...
```

### Mistake 7: Integer mutation in nested functions

```python
# ❌ WRONG in Python 3:
max_val = 0
def dfs(node):
    max_val = max(max_val, node.val)   # Creates LOCAL max_val!

# ✅ FIX 1: Use list
max_val = [0]
def dfs(node):
    max_val[0] = max(max_val[0], node.val)

# ✅ FIX 2: Use nonlocal
def outer():
    max_val = 0
    def dfs(node):
        nonlocal max_val
        max_val = max(max_val, node.val)
```

---

## 16. PYTHON TEMPLATES TO MEMORIZE

### The Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
```

### Template 1: Generic DFS (Bottom-Up)

```python
def solve(root):
    def dfs(node):
        if not node:
            return BASE_VALUE   # 0, -1, None, float('-inf'), etc.
        
        left  = dfs(node.left)
        right = dfs(node.right)
        
        # Combine left, right, node.val
        return COMBINE(left, right, node.val)
    
    return dfs(root)
```

### Template 2: DFS with Global State

```python
def solve(root):
    result = [INITIAL_VALUE]   # Use list for mutability
    
    def dfs(node):
        if not node:
            return BASE_VALUE
        
        left  = dfs(node.left)
        right = dfs(node.right)
        
        # Update global answer
        result[0] = max(result[0], SOME_EXPRESSION)
        
        # Return something useful to parent
        return RETURN_VALUE
    
    dfs(root)
    return result[0]
```

### Template 3: DFS Top-Down (Passing state down)

```python
def solve(root):
    def dfs(node, extra_info):
        if not node:
            return BASE_CASE
        
        # Use extra_info + node.val
        new_info = UPDATE(extra_info, node.val)
        
        left  = dfs(node.left,  new_info)
        right = dfs(node.right, new_info)
        
        return COMBINE(left, right)
    
    return dfs(root, INITIAL_INFO)
```

### Template 4: BFS Level-Order

```python
from collections import deque

def solve(root):
    if not root:
        return []
    
    result = []
    queue  = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        
        result.append(level)
        # OR: process level here (min, max, average, etc.)
    
    return result
```

### Template 5: Backtracking (Path collection)

```python
def solve(root, target):
    result = []
    
    def dfs(node, path, state):
        if not node:
            return
        
        path.append(node.val)          # Choose
        state = UPDATE(state, node.val)
        
        if IS_GOAL(node, state):
            result.append(list(path))  # Record (copy!)
        
        dfs(node.left,  path, state)
        dfs(node.right, path, state)
        
        path.pop()                     # Unchoose (backtrack)
    
    dfs(root, [], INITIAL_STATE)
    return result
```

### Template 6: BST Validation

```python
def is_valid_bst(root):
    def validate(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return (validate(node.left,  lo,       node.val) and
                validate(node.right, node.val, hi))
    
    return validate(root, float('-inf'), float('inf'))
```

### Template 7: Serialization / Deserialization

```python
def serialize(root):
    res = []
    def dfs(node):
        if not node:
            res.append('N'); return
        res.append(str(node.val))
        dfs(node.left); dfs(node.right)
    dfs(root)
    return ','.join(res)

def deserialize(data):
    vals = iter(data.split(','))
    def build():
        v = next(vals)
        if v == 'N': return None
        node = TreeNode(int(v))
        node.left  = build()
        node.right = build()
        return node
    return build()
```

---

## 17. LC 75 TREES ROADMAP

### The LC 75 Tree Problems

```
LC 75 Trees Section (all problems):
  104. Maximum Depth of Binary Tree       ← START HERE
  872. Leaf-Similar Trees
  1448. Count Good Nodes in Binary Tree
  700. Search in a Binary Search Tree
  98.  Validate Binary Search Tree
  450. Delete Node in a BST
  543. Diameter of Binary Tree
  1161. Maximum Level Sum of Binary Tree
  199. Binary Tree Right Side View
  1372. Longest ZigZag Path in a Binary Tree
  1026. Maximum Difference Between Node and Ancestor
  236. Lowest Common Ancestor of a Binary Tree
  226. Invert Binary Tree              ← Bonus (often in LC 75 variants)
```

---

### TIER 1 — WARM UP (Do these first, in order)

---

#### 🟢 LC 104 — Maximum Depth of Binary Tree

**Intuition:** Height of tree. Classic bottom-up recursion.

**Pattern:** Post-order, bottom-up aggregation.

**When to use:** Any "how tall / how deep" question.

```
        3
       / \
      9  20
        /  \
       15   7

depth(15)=1, depth(7)=1
depth(20)=2, depth(9)=1
depth(3) = 1 + max(1, 2) = 3
```

```python
# Recursive
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Iterative BFS
def max_depth_bfs(root):
    if not root:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
    return depth
```

**Pitfalls:**
- Return `0` for null (not `-1`) — this problem counts NODES not edges.
- BFS iterative is clean and avoids stack overflow for huge trees.

---

#### 🟢 LC 226 — Invert Binary Tree

**Intuition:** Swap left and right children at EVERY node.

**Pattern:** Pre-order top-down, or post-order (both work).

```
    4              4
   / \    →       / \
  2   7          7   2
 / \ / \        / \ / \
1  3 6  9      9  6 3  1
```

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

# OR post-order (invert children first, then swap):
def invert_tree_post(root):
    if not root:
        return None
    left  = invert_tree_post(root.left)
    right = invert_tree_post(root.right)
    root.left, root.right = right, left
    return root
```

**Pitfalls:**
- Both pre and post order work. Pre-order is more intuitive.
- Return `root` at the end — caller needs the (modified) node back.

---

#### 🟢 LC 872 — Leaf-Similar Trees

**Intuition:** Collect all leaf values in left-to-right order for both trees, compare.

**Pattern:** DFS to collect leaves (in-order left-to-right).

```python
def leaf_similar(root1, root2):
    def get_leaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]     # Leaf!
        return get_leaves(node.left) + get_leaves(node.right)
    
    return get_leaves(root1) == get_leaves(root2)
```

**Pitfalls:**
- List concatenation is O(n) each time — for large trees, use a list + append.
- Don't forget: leaf = node with no left AND no right child.

---

### TIER 2 — CORE PATTERNS

---

#### 🟡 LC 1448 — Count Good Nodes in Binary Tree

**Intuition:** A node is "good" if no node on the path from root to it has a GREATER value.
Pass the running maximum downward.

**Pattern:** Top-down DFS, passing state down.

```
        3
       / \
      1   4
     /   / \
    3   1   5

Good nodes: 3 (root), 3 (left-left, path max=3), 4, 5
Count = 4
```

```python
def good_nodes(root):
    def dfs(node, max_so_far):
        if not node:
            return 0
        
        is_good = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        
        return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)
    
    return dfs(root, float('-inf'))
```

**Pitfalls:**
- Initialize `max_so_far = float('-inf')` so root is always good.
- `>=` not `>`: node equal to max is still "good".

---

#### 🟡 LC 700 — Search in a Binary Search Tree

**Intuition:** BST property: go left if target < node, right if target > node.

**Pattern:** BST search.

```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)
```

**Pitfalls:**
- Never search both subtrees — that wastes the BST property.
- Return the SUBTREE rooted at found node, not just the value.

---

#### 🟡 LC 543 — Diameter of Binary Tree

(Full solution shown in Section 7)

**Pattern:** Post-order, global max updated during recursion.

**Key insight:** The diameter through a node = left_depth + right_depth.
The function RETURNS depth but UPDATES global diameter.

```python
def diameter_of_binary_tree(root):
    ans = [0]
    def depth(node):
        if not node: return 0
        l = depth(node.left)
        r = depth(node.right)
        ans[0] = max(ans[0], l + r)
        return 1 + max(l, r)
    depth(root)
    return ans[0]
```

**Pitfalls:**
- The diameter may not pass through the root! That's why we track global max.
- Return `depth`, not `diameter`, from the recursive function.

---

#### 🟡 LC 199 — Binary Tree Right Side View

**Intuition:** For each level, take the LAST (rightmost) node's value.

**Pattern:** BFS level-order, take last element of each level.

```
        1        ← see 1
       / \
      2   3      ← see 3
       \   \
        5   4    ← see 4

Result: [1, 3, 4]
```

```python
def right_side_view(root):
    if not root:
        return []
    result = []
    queue  = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:        # Last node in this level
                result.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
    
    return result

# DFS Alternative: right-first DFS, track depth
def right_side_view_dfs(root):
    result = []
    def dfs(node, depth):
        if not node: return
        if depth == len(result):           # First time at this depth
            result.append(node.val)
        dfs(node.right, depth + 1)        # Right first!
        dfs(node.left,  depth + 1)
    dfs(root, 0)
    return result
```

**Pitfalls:**
- BFS: Take the LAST node per level, not the rightmost child.
- DFS: Go RIGHT first so "first visit at depth d" = rightmost node.

---

#### 🟡 LC 1161 — Maximum Level Sum of Binary Tree

**Intuition:** Sum all nodes at each level, return the level with max sum.

**Pattern:** BFS level-order, track level sums.

```python
def max_level_sum(root):
    if not root:
        return 0
    
    max_sum   = float('-inf')
    max_level = 0
    level     = 0
    queue     = deque([root])
    
    while queue:
        level     += 1
        level_sum  = 0
        
        for _ in range(len(queue)):
            node      = queue.popleft()
            level_sum += node.val
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        
        if level_sum > max_sum:
            max_sum   = level_sum
            max_level = level
    
    return max_level
```

**Pitfalls:**
- Level numbering starts at 1, not 0 (problem statement says so).
- Node values can be negative! Initialize `max_sum = float('-inf')`.

---

### TIER 3 — HARDER PATTERNS

---

#### 🔴 LC 98 — Validate Binary Search Tree

(Full solution in Section 10)

**Pattern:** Top-down DFS with min/max bounds.

**Key insight:** Not just immediate children — entire subtree must satisfy bounds.

```python
def is_valid_bst(root):
    def validate(node, lo, hi):
        if not node: return True
        if not (lo < node.val < hi): return False
        return (validate(node.left,  lo, node.val) and
                validate(node.right, node.val, hi))
    return validate(root, float('-inf'), float('inf'))
```

**Pitfalls:**
- Use `lo < val < hi` (strict inequalities) — BST doesn't allow duplicates.
- Pass `float('-inf')` and `float('inf')` as initial bounds.

---

#### 🔴 LC 450 — Delete Node in a BST

**Intuition:** Find the node. Then handle 3 cases:
1. Leaf → just remove it (return None).
2. One child → replace node with that child.
3. Two children → replace with in-order successor (smallest in right subtree),
   then delete that successor from right subtree.

```
        5
       / \
      3   6
     / \   \
    2   4   7

Delete 3:
  in-order successor of 3 = 4 (smallest in right subtree of 3)
  Replace 3.val with 4, delete 4 from right subtree.

        5
       / \
      4   6
     /     \
    2       7
```

```python
def delete_node(root, key):
    if not root:
        return None
    
    if key < root.val:
        root.left  = delete_node(root.left,  key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Found the node to delete
        if not root.left:   return root.right   # Case 1 or 2
        if not root.right:  return root.left    # Case 2
        
        # Case 3: two children — find in-order successor
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val   = successor.val                   # Copy value up
        root.right = delete_node(root.right, root.val)  # Delete successor
    
    return root
```

**Pitfalls:**
- Always `return root` at the end — maintains the linked structure.
- In-order successor = leftmost node in right subtree.
- In-order predecessor = rightmost node in left subtree (alternative).

---

#### 🔴 LC 1026 — Maximum Difference Between Node and Ancestor

**Intuition:** For each node, the max difference = max(|node - ancestor|) for all ancestors.
This = max(node.val - min_ancestor, max_ancestor - node.val).
Pass min and max seen so far down the tree.

```python
def max_ancestor_diff(root):
    def dfs(node, curr_min, curr_max):
        if not node:
            return curr_max - curr_min
        
        curr_min = min(curr_min, node.val)
        curr_max = max(curr_max, node.val)
        
        left  = dfs(node.left,  curr_min, curr_max)
        right = dfs(node.right, curr_min, curr_max)
        
        return max(left, right)
    
    return dfs(root, root.val, root.val)
```

**Pitfalls:**
- At null node, return `curr_max - curr_min` (the best diff found on this path).
- Initialize with `root.val` for both min and max.

---

#### 🔴 LC 236 — Lowest Common Ancestor of a Binary Tree

(Full solution in Section 9)

**Pattern:** Post-order. If both sides return something, current node is LCA.

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left  = lowest_common_ancestor(root.left,  p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)
```

**Pitfalls:**
- The LCA of a node with itself is itself (re-read the problem — a node can be
  ancestor of itself). The `root == p` base case handles this.
- Trust that if `p` is found deep in left subtree, the recursion returns it.

---

#### 🔴 LC 1372 — Longest ZigZag Path in a Binary Tree

**Intuition:** At each node, track the ZigZag length if you came from LEFT or RIGHT.
If you came from left (parent went left to reach you), next step should go RIGHT.

```python
def longest_zig_zag(root):
    ans = [0]
    
    def dfs(node, direction, length):
        if not node: return
        ans[0] = max(ans[0], length)
        
        if direction == 'left':
            dfs(node.left,  'left',  1)        # Reset: go same direction
            dfs(node.right, 'right', length+1) # Continue ZigZag
        else:
            dfs(node.left,  'left',  length+1) # Continue ZigZag
            dfs(node.right, 'right', 1)        # Reset: go same direction
    
    dfs(root.left,  'left',  1)
    dfs(root.right, 'right', 1)
    return ans[0]
```

**Alternative cleaner approach:**

```python
def longest_zig_zag(root):
    ans = [0]
    
    # Returns (go_left_length, go_right_length)
    def dfs(node):
        if not node:
            return -1, -1
        
        left_left,  left_right  = dfs(node.left)
        right_left, right_right = dfs(node.right)
        
        # If we go left from current, the chain continues from left child's right
        go_left  = left_right + 1
        # If we go right from current, the chain continues from right child's left
        go_right = right_left + 1
        
        ans[0] = max(ans[0], go_left, go_right)
        return go_left, go_right
    
    dfs(root)
    return ans[0]
```

**Pitfalls:**
- ZigZag length = number of EDGES, not nodes.
- When you go the same direction twice, reset to 1 (not 0).

---

### PATTERN RECOGNITION GUIDE

```
┌───────────────────────────────────────────────────────────────────┐
│ PROBLEM TYPE                   │ APPROACH                         │
├───────────────────────────────────────────────────────────────────┤
│ "Height / depth / max depth"   │ Post-order DFS, return height    │
│ "Level-by-level"               │ BFS with level_size snapshot     │
│ "Right/left side view"         │ BFS last-per-level OR right-DFS  │
│ "Path sum (root-to-leaf)"      │ DFS top-down, subtract target    │
│ "All paths"                    │ DFS + backtracking (append/pop)  │
│ "Diameter / longest path"      │ Post-order, global max + return  │
│ "Is balanced?"                 │ Post-order, sentinel -1 trick    │
│ "LCA"                          │ Post-order, return p/q/LCA       │
│ "Validate BST"                 │ DFS with (min, max) bounds       │
│ "BST search/insert/delete"     │ BST property: go left or right   │
│ "Build tree from traversals"   │ Pre[0]=root, split by inorder    │
│ "Serialize/deserialize"        │ Pre-order DFS with null markers  │
│ "Good nodes / path maximum"    │ DFS top-down, pass running max   │
│ "ZigZag / directional path"    │ DFS with direction state         │
└───────────────────────────────────────────────────────────────────┘
```

---

### INTERVIEW EXECUTION CHECKLIST

When you get a tree problem in an interview:

```
□ 1. Ask: "Can the tree be empty? Can values be negative?"
□ 2. Draw a simple example (3–5 nodes). Trace manually.
□ 3. Identify the pattern (DFS/BFS? Top-down/Bottom-up?)
□ 4. Write the base case FIRST (null check).
□ 5. Write the recursive calls (trust them).
□ 6. Write the combine step.
□ 7. Trace your code on a single-node tree and empty tree.
□ 8. State time and space complexity.
   → Time:  O(n) if you visit every node once.
   → Space: O(h) recursive, O(n) BFS queue worst case.
```

### MNEMONICS

```
"PRE means before, IN means inside, POST means after."
→ Where ROOT appears in the traversal.

"BFS = Breadth = WIDE = level by level"
"DFS = Depth = DEEP = one branch at a time"

"BST: Left is Less, Right is gReateR"

"Backtrack: append → recurse → POP"

"LCA: if both sides return something, I'M the answer."

"Diameter: I update global at each node, but I return depth."

"Validate BST: not just children — pass bounds down."
```

---
