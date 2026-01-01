# Graph Data Structure

A graph is a node with vertices.

Node represents things while edges represent connections between things.

3 ways of Graph representation in Python:
1. Adjacency List
2. Adjacency Matrix
3. Edge List

## Adjacency List

An adjacency list stores each node and the list of nodes it is connected to.

```
A ── B
│
C
```

The above graph is represented in the following code:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
```

```python
from collections import defaultdict

graph = defaultdict(list)

graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('A')
graph['C'].append('A')
```

### Graphs with weights

```
A --5--> B
A --2--> C
```

```python
graph = {
    'A': [( 'B', 5 ), ( 'C', 2 )],
    'B': [],
    'C': []
}
```

# Clone Graph problem 

You're given one node of a connected undirected graph. Each node has a 'val' and a list of neighbors.

Creating a clone mean having no shared copies.

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []
```
