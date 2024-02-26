"""
Q4. Implement the following undirected unweighted graph using class, methods, and data structures of Python.
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
        self.adj[head].append(tail)

    def __str__(self) -> str:
        res = ""
        for node in self.adj:
            for neighbor in self.adj[node]:
                res += f"({node}->{neighbor})\t"
            res += "\n"
        return res


if __name__ == "__main__":
    g = Graph()

    print("Enter start, end, 0 to end")
    while True:
        inp = input(": ")
        if inp == "0":
            break
        start, end = inp.split(" ")
        g.insert(start, end)

    print(g)

# {'A': ['B', 'C', 'E'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D', 'E'], 'E': ['A', 'C'], 'D': ['C']}