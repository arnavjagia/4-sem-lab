"""
Q1. Implement the following directed unweighted graph using class, methods, and data structures of Python.
"""

class Graph:
    def __init__(self):
        self.adjlist = dict()
    
    def insert(self, start, end):
        if start not in self.adjlist:
            self.adjlist[start] = []
        self.adjlist[start].append(end)

    def display_edges(self):
        for start, endlist in self.adjlist.items():
            for end in endlist:
                print(f'({start} -> {end})', end=' ')
            print()


if __name__ == '__main__':
    g = Graph()

    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    for edge in edges:
        g.insert(edge[0], edge[1])
    
    g.display_edges()

"""
(0 -> 1) 
(1 -> 2) 
(2 -> 0) (2 -> 1) 
(3 -> 2) 
(4 -> 5) 
(5 -> 4)
"""
