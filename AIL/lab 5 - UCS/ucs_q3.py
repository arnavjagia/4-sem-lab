class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True)

    def extract_min(self):
        if not self.queue:
            return None
        return self.queue.pop()[1]

    def is_empty(self):
        return len(self.queue) == 0

class Graph:
    def __init__(self, adjlist):
        self.adj = adjlist

    def neighbors(self, node):
        return self.adj[node]

def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.insert(0, (start, [], 0))  # Priority is the cost of the path
    explored = set()

    while not frontier.is_empty():
        current_node, path, cost = frontier.extract_min()

        if current_node == goal:
            return cost, path + [current_node]

        explored.add(current_node)

        for neighbor, neighbor_cost in graph.neighbors(current_node).items():
            if neighbor not in explored:
                new_cost = cost + neighbor_cost
                frontier.insert(new_cost, (neighbor, path + [current_node], new_cost))

    return None, None

if __name__ == "__main__":
    graph = {
        'maldon':{'tiptree': 8},
        'tiptree':{'feering': 3, 'clacton': 29},
        'feering':{'maldon': 11, 'blaxhali': 46},
        'clacton':{'maldon': 40, 'harwich': 17},
        'harwich':{'tiptree': 31, 'blaxhali': 40, 'dunwich': 53},
        'blaxhali':{'dunwich': 15},
        'dunwich':{'blaxhali': 17},
    }

    g = Graph(graph)
    start_node = 'maldon'
    goal_node = 'dunwich'

    min_cost, path = uniform_cost_search(g, start_node, goal_node)

    if path:
        print("Best path from", start_node, "to", goal_node, ":", path)
        print("Minimum cost:", min_cost)
    else:
        print("No path found from", start_node, "to", goal_node)

