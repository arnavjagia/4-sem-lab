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


def uniform_cost_search(graph, start, goals):
    frontier = PriorityQueue()
    frontier.insert(0, (start, [], 0))  # Priority is the cost of the path
    explored = set()

    while not frontier.is_empty():
        current_node, path, cost = frontier.extract_min()

        if current_node in goals:
            return current_node, path + [current_node], cost

        explored.add(current_node)

        for neighbor, neighbor_cost in graph.neighbors(current_node).items():
            if neighbor not in explored:
                new_cost = cost + neighbor_cost
                frontier.insert(new_cost, (neighbor, path + [current_node], new_cost))

    return None, None, None


if __name__ == "__main__":
    graph = {
        "s": {"a": 5, "b": 9, "d": 6},
        "a": {"b": 3, "g1": 9},
        "b": {"a": 2, "c": 1},
        "c": {"s": 6, "f": 7, "g2": 5},
        "d": {"c": 2, "e": 2},
        "e": {"g3": 7},
        "f": {"d": 2, "g3": 8},
        "g1": {},
        "g2": {},
        "g3": {},
    }
    g = Graph(graph)
    start_node = "s"
    goal_nodes = {"g1", "g2", "g3"}

    goal, path, min_cost = uniform_cost_search(g, start_node, goal_nodes)

    if goal:
        print("Goal node with least cumulative cost:", goal)
        print("Best path:", path)
        print("Minimum cost:", min_cost)
    else:
        print("No path found from", start_node, "to any of the goal nodes", goal_nodes)
