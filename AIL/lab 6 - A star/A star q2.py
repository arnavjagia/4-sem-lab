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

    def a_star(self, start, goals):
        dist = {v: float('inf') for v in self.adj} # initial distance estimates
        frontier = PriorityQueue()

        dist[start] = 0
        frontier.insert(0, start) # "frontier" to be explored 
        prev = {v: None for v in self.adj} # for storing lowest cost parents

        closed = set()

        while frontier:
            priority_current, current = frontier.extract_min()
            
            if current in goals:
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

        return self.reconstruct_path(start, current, prev)

if __name__ == "__main__":
    h_dist = {
        'A': 7,
        'B': 3,
        'C': 4,
        'D': 6,
        'E': 5,
        'F': 6,
        'G1': 0,
        'G2': 0,
        'G3': 0,
        'S': 5,
    }

    Graph_nodes = {
        'A': [('B', 3), ('G1', 9)],
        'B': [('A', 2), ('C', 1)],
        'C': [('F', 7), ('G2', 5), ('S', 6)],
        'D': [('C', 2), ('E', 2), ('S', 1)],
        'E': [('G3', 7)],
        'F': [('D', 2), ('G3', 8)],
        'G1': [],
        'G2': [],
        'G3': [],
        'S': [('A', 7), ('B', 9), ('D', 6)],
    }

    g = Graph(Graph_nodes, h_dist)
    print(g.a_star('S', {'G1', 'G2', 'G3'})) # ['S', 'D', 'C', 'G2']