"""
Q1. Implement the following directed unweighted graph using class, methods, and data structures of Python.
"""


class Graph:
    def __init__(self, adj: dict = {}):
        self.adj = adj

    def insert(self, tail, head):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append(head)

        if head not in self.adj:
            self.adj[head] = []

    def __str__(self) -> str:
        res = ""
        for node in self.adj:
            for neighbor in self.adj[node]:
                res += f"({node}->{neighbor})\t"
            res += "\n"
        return res

if __name__ == "__main__":
    g = Graph()

    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    for edge in edges:
        g.insert(edge[0], edge[1])

    print(g)
