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

class Graph:
    def __init__(self, adjlist : dict = {}):
        self.adj = adjlist

    def __str__(self):
        res = ""
        for tail, headlist in self.adj.items():
            for head in headlist:
                res += f"({tail} -> {head}, {headlist[head]})\t"
            res += "\n"
        return res
    
    def bfs(self, start):
        queue = Deque()
        queue.enqueue((start, [start]))

        while queue.arr:
            (node, path) = queue.dequeue()
            for next_node in set(graph[node]) - set(path):
                if len(path) + 1 == len(graph):
                    yield path + [next_node]
                else:
                    queue.enqueue((next_node, path + [next_node]))

    def tsp_bfs(self, start):
        shortest_path = None
        shortest_path_length = float('inf')

        for path in self.bfs(start):
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
g = Graph(graph)
print(g.tsp_bfs('C'))


"""
(['C', 'B', 'A', 'D'], 10)
"""
