import networkx as nx

G = nx.Graph()
G.add_edges_from([
    ("Switch-1", "Server-A"),
    ("Switch-1", "Server-B"),
    ("Switch-2", "Server-C"),
    ("Server-A", "VM-01"),
])

# Find all paths between two nodes
print(list(nx.all_simple_paths(G, source="Switch-1", target="VM-01")))


dependencies = {
    "frontend": ["api"],
    "api": ["database", "auth"],
    "auth": ["ldap"],
    "database": [],
    "ldap": []
}

G = nx.DiGraph(dependencies)
print(list(nx.topological_sort(G)))  # Safe startup order
