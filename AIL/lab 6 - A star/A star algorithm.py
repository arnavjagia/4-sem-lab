"""
https://www.baeldung.com/cs/a-star-algorithm
"""

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(reverse = True)

    def extract_min(self) -> tuple[int, int]:
        if not self.queue:
            return None
        return self.queue.pop()
    
    def is_empty(self):
        return len(self.queue) == 0

class Graph:
    def __init__(self, adjlist : dict = {}, heuristic : dict = {}):
        self.adj = adjlist
        self.heuristics = heuristic

    def reconstruct_path(self, start, goal, prev):
        path = []
        current = goal
        while current != start:
            path = [current] + path
            current = prev[current]
        return [start] + path

    def heuristic(self, node):
        return self.heuristics[node]

    def a_star(self, start, goal):
        dist = {v: float('inf') for v in self.adj} # initial distance estimates
        frontier = PriorityQueue()

        dist[start] = 0
        frontier.insert(0, start) # "frontier" to be explored 
        prev = {v: None for v in self.adj} # for storing lowest cost parents

        closed = set()

        while frontier:
            priority_current, current = frontier.extract_min()
            
            if current == goal:
                break

            if current in closed:
                continue
            closed.add(current)

            for neighbor, edge_weight in self.adj[current]:
                alt_dist = dist[current] + edge_weight
                if alt_dist < dist[neighbor]:
                    dist[neighbor] = alt_dist
                    prev[neighbor] = current

                    # this is the only thing that's different from dijkstra's:
                    priority = alt_dist + self.heuristic(neighbor)
                    frontier.insert(priority, neighbor)

        return self.reconstruct_path(start, goal, prev)

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