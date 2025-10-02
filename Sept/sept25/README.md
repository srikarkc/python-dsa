# Graphs

Graphs have vertex / vertices and are connected by edges. 

The edges might have weights to them so the path is not necessarily the shortest. Think of network routing protocols.

They can be represented in an adjacency matrix but the downside is that there will be a lot of zeros and this causes higher storage utilization.

The more efficient way to store them is in an adjacency matrix.

We will get a ValueError when we try to remove an item that is not in a list. 

```python
try:
    self.adj_list[v1].remove(v2)
    self.adj_list[v2].remove(v1)
except ValueError:
    pass
return True
```