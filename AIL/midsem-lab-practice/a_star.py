class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(reverse = True)

    def extract_min(self) -> tuple[int, int]:
        if not self.queue:
            return None
        return self.queue.pop()[1]
    
    def is_empty(self):
        return len(self.queue) == 0

class Graph:
    def __init__(self, adjlist : dict = {}, heuristic : dict = {}):
        self.adj = adjlist
        self.heuristics = heuristic

    def heuristic(self, node):
        return self.heuristics[node]
    
    def a_star(self, start, goal):
        q = PriorityQueue()
        q.insert(0, (start, [start], 0))
        visited = set()

        while not q.is_empty():
            (current, path, path_length) = q.extract_min()
            if current == goal:
                return path
            visited.add(current)

            if current in self.adj:
                for neighbor, weight in self.adj[current]:
                    if neighbor not in path:
                        q.insert(
                            path_length + weight + self.heuristic(neighbor),
                            (neighbor, path + [neighbor], path_length + weight),
                        )
        return None

if __name__ == "__main__":
    h_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }

    Graph_nodes = {
        'A': [('B', 2), ('E', 3)],
        'B': [('A', 2), ('C', 1), ('G', 9)],
        'C': [('B', 1)],
        'D': [('E', 6), ('G', 1)],
        'E': [('A', 3), ('D', 6)],
        'G': [('B', 9), ('D', 1)]
    }

    graph1 = Graph(Graph_nodes, h_dist)
    print(graph1.a_star('A', 'G')) # ['A', 'E', 'D', 'G']