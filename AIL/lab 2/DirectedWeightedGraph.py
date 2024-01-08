"""
Q2. Implement the following directed weighted graph using class, methods, and data structures of Python.
"""

class Edge:
    def __init__(self, start, end, weight):
        self.start, self.end, self.weight = start, end, weight

class Graph:
    def __init__(self):
        self.adj_list = dict()

    def insert(self, start, end, weight):
        if not start in self.adj_list:
            self.adj_list[start] = []
        self.adj_list[start].append(Edge(start, end, weight))
    
    def describe(self):
        for key in self.adj_list:
            for e in self.adj_list[key]:
                print(f'({e.start} --> {e.end}, {e.weight})', end=' ')
            print()

if __name__ == '__main__':
    G = Graph()

    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10), (4, 5, 1),
        (5, 4, 3)]
    for edge in edges:
        G.insert(edge[0], edge[1], edge[2])

    G.describe()
