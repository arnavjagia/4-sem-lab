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

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        (node, path) = queue.popleft()
        for next_node in set(graph[node]) - set(path):
            if len(path) + 1 == len(graph):
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

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
