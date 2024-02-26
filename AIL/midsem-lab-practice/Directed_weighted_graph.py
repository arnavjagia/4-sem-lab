"""
Q2. Implement the following directed weighted graph using class, methods, and data structures of Python.
"""


class Graph:
    def __init__(self, adj: dict = {}):
        self.adj = adj

    def insert(self, tail, head, weight):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append((weight, head))

        if head not in self.adj:
            self.adj[head] = []

    def __str__(self) -> str:
        res = ""
        for node in self.adj:
            for neighbor in self.adj[node]:
                res += f"({node}->{neighbor[1]}, {neighbor[0]})\t"
            res += "\n"
        return res

if __name__ == "__main__":
    g = Graph()

    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10), (4, 5, 1),
        (5, 4, 3)]
    for edge in edges:
        g.insert(edge[0], edge[1], edge[2])

    print(g)
