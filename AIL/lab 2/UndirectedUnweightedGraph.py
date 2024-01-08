"""
Q3. Implement the following undirected weighted graph using class, methods, and data structures of Python.
Print the adjacency list and adjacency matrix.
"""

class UndirectedGraph:
    def __init__(self):
        self.adjlist = dict()

    def insert(self, p, q, reverse=True):
        if p not in self.adjlist:
            self.adjlist[p] = []
        self.adjlist[p].append(q) 

        if reverse:
            self.insert(q, p, False)

    def adj_matrix(self):
        matrix = []

        for i in nodes:
            row = [1 if j in self.adjlist[i] else 0 for j in nodes]
            matrix.append(row)

        return matrix

g = UndirectedGraph()

print('Enter node pairs, enter 0 to end')

i = input(': ')
while i != '0':
    p, q = i.split()
    g.insert(p, q)
    i = input(': ')

print(g.adjlist)
print(g.adj_matrix())
