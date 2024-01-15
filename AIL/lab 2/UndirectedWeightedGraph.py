"""
UndirectedWeightedGraph
"""
class Edge:
    def __init__(self, start, end, weight):
        self.start, self.end, self.weight = start, end, weight

class UndirectedWeightedGraph:
    def __init__(self):
        self.adj_list = dict()

    def insert(self, p, q, weight, reciprocity=True):
        # create edge from p to q
        if p not in self.adj_list:
            self.adj_list[p] = []
        self.adj_list[p].append(Edge(p, q, weight)) 

        # create edge from q to p
        # `reciprocity` set to False to avoid infinite recursion
        if reciprocity:
            self.insert(q, p, weight, reciprocity=False) 

    def get_adj_matrix(self):
        nodes = sorted(self.adj_list) # sorted list of nodes
        matrix = []

        for i in nodes:
            row = [1 if j in self.adj_list[i] else 0 for j in nodes]
            matrix.append(row)

        return matrix

    def describe(self):
        for key in self.adj_list:
            for e in self.adj_list[key]:
                print(f'({e.start} -- {e.end}, {e.weight})', end=' ')
            print()

if __name__ == '__main__':
    G = UndirectedWeightedGraph()

    print('Enter node pairs with weight, enter 0 to end')

    i = input('> ')
    while i != '0':
        p, q, w = i.split()
        G.insert(p, q, int(w))
        i = input('> ')

    G.describe()
