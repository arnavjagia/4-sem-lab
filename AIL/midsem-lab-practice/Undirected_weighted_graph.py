"""
Q3. Implement the following undirected weighted graph using class, methods, and data structures of Python.
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
        self.adj[head].append((weight, tail))

    def __str__(self) -> str:
        res = ""
        for node in self.adj:
            for neighbor in self.adj[node]:
                res += f"({node}->{neighbor[1]}, {neighbor[0]})\t"
            res += "\n"
        return res


if __name__ == "__main__":
    g = Graph()

    print("Enter start, end, weight, 0 to end")
    while True:
        inp = input(": ")
        if inp == '0':
            break
        start, end, weight = inp.split(" ")
        g.insert(start, end, weight)

    print(g)
