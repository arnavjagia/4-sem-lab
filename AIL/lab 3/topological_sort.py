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

    def topological_sort(self, start: int, visited: list[int], sort: list[int], vertices: list[int]) -> list[int]:
        """Perform topological sort on a directed acyclic graph."""
        current = start
        # add current to visited
        visited.append(current)
        neighbors = edges[current]
        for neighbor in neighbors:
            # if neighbor not in visited, visit
            if neighbor not in visited:
                sort = self.topological_sort(neighbor, visited, sort, vertices)
        # if all neighbors visited add current to sort
        sort.append(current)
        # if all vertices haven't been visited select a new one to visit
        if len(visited) != len(vertices):
            for vertice in vertices:
                if vertice not in visited:
                    sort = self.topological_sort(vertice, visited, sort, vertices)
        # return sort
        return sort

if __name__ == '__main__':
    g = Graph()
    # edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    edges = [(5,0),(4,0),(5,2),(2,3),(3,1),(4,1)]
    for edge in edges:
        g.insert(edge[0], edge[1])

    vertices = list(g.adjlist.keys())
    sort = g.topological_sort(4, [], [], vertices)
    print(sort)
