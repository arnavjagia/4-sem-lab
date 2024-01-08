class UndirectedGraph:
    def __init__(self):
        self.adj_list = dict()

    def insert(self, p, q, reciprocity=True):
        # create edge from p to q
        if p not in self.adj_list:
            self.adj_list[p] = []
        self.adj_list[p].append(q) 

        # create edge from q to p
        # `reciprocity` set to False to avoid infinite recursion
        if reciprocity:
            self.insert(q, p, reciprocity=False) 

    def get_adj_matrix(self):
        nodes = sorted(self.adj_list) # sorted list of nodes
        matrix = []

        for i in nodes:
            row = [1 if j in self.adj_list[i] else 0 for j in nodes]
            matrix.append(row)

        return matrix


if __name__ == '__main__':
    G = UndirectedGraph()

    print('Enter node pairs, enter 0 to end')

    i = input('> ')
    while i != '0':
        p, q = i.split()
        G.insert(p, q)
        i = input('> ')
    
    print(G.adj_list)
    print(G.get_adj_matrix())
