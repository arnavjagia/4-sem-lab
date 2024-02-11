"""
https://www.baeldung.com/cs/a-star-algorithm
"""

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(reverse = True)

    def extract_min(self):
        if not self.queue:
            return None
        return self.queue.pop()[1]
    
    def is_empty(self):
        return False if self.queue else return True

class Graph:
    def __init__(self, adjlist : dict = {}, heuristic : dict = {}):
        self.adj = adjlist
        self.heuristic = heuristic

    def neighbors(self, node):
        return self.adj[node]
        
    def a_star(self):
        frontier = PriorityQueue()
        
        
