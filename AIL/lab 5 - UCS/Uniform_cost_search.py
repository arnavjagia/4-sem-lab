"""
Uniform Cost Search algorithm
https://www.baeldung.com/cs/uniform-cost-search-vs-best-first-search
https://www.javatpoint.com/ai-uninformed-search-algorithms
https://stackoverflow.com/questions/407734/a-generic-priority-queue-for-python
https://github.com/TheAlgorithms/Python/blob/master/graphs/dijkstra_algorithm.py
https://www.baeldung.com/cs/uniform-cost-search-vs-dijkstras

W YouTube video
https://youtu.be/dRMvK76xQJI?si=8W7SFb4bqYE_gdpv
"""

# implemented using priority queue
# UCS is equivalent to BFS when path cost of all edges are same
# BFS focuses on shortest path to search a node
# UCS focuses on least cost path from root node to goal node

# TODO 1: make priority queue using heap
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
        's': {1: 2, 3: 5},
        1: {'g': 1},
        2: {1: 4},
        3: {1: 5, 4: 6, 'g': 2},
        4: {2: 4, 5: 3},
        5: {2: 6, 'g': 3},
        'g': {4: 7},
    }

    g = Graph(graph)
    start_node = 's'
    goal_node = 'g'

    min_cost, path = uniform_cost_search(g, start_node, goal_node)

    if path:
        print("Best path from", start_node, "to", goal_node, ":", path)
        print("Minimum cost:", min_cost)
    else:
        print("No path found from", start_node, "to", goal_node)

