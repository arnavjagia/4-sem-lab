"""
Write python code for Traveling Salesman Problem (TSP) using Breadth First Search 
(BFS). Graph Given Below.
graph = {
 'A': {'B': 2, 'C': 3, 'D': 1},
 'B': {'A': 2, 'C': 4, 'D': 2},
 'C': {'A': 3, 'B': 4, 'D': 3},
 'D': {'A': 1, 'B': 2, 'C': 3}
}
"""

class Deque:
    def __init__(self):
        self.arr = []
        
    def enqueue(self, ele):
        self.arr.append(ele)
        
    def dequeue(self):
        return self.arr.pop(0)
        
    def __str__(self):
        res = "Queue: "
        for ele in self.arr:
            res += str(ele) + " "
        return res

def bfs(graph, start):
    visited = set()
    queue = Deque()
    queue.enqueue((start, [start]))

    while queue.arr:
        (node, path) = queue.dequeue()
        for next_node in set(graph[node]) - set(path):
            if len(path) + 1 == len(graph):
                yield path + [next_node]
            else:
                queue.enqueue((next_node, path + [next_node]))

def tsp_bfs(graph, start):
    shortest_path = None
    shortest_path_length = float('inf')

    for path in bfs(graph, start):
        path_length = sum(graph[path[i-1]][path[i]] for i in range(len(path)))
        if path_length < shortest_path_length:
            shortest_path = path
            shortest_path_length = path_length

    return shortest_path, shortest_path_length

# example usage:
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}
print(tsp_bfs(graph, 'C'))

"""
(['C', 'B', 'A', 'D'], 10)
"""
