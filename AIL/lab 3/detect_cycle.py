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

    def detect_cycle(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            if node in self.adjlist:
                for neighbor in self.adjlist[node]:
                    if neighbor not in visited:
                        if dfs(neighbor):
                            return True
                    elif neighbor in stack:
                        return True

            stack.remove(node)
            return False

        for node in self.adjlist:
            if node not in visited:
                if dfs(node):
                    return True

        return False

if __name__ == '__main__':
    g = Graph()
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
    for edge in edges:
        g.insert(edge[0], edge[1])

    if g.detect_cycle():
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")

"""
The graph contains a cycle.
"""