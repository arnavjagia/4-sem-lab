"""
Consider the following directed graph for detecting cycles in the graph using BFS 
algorithm using Python.
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
    def __init__(self):
        self.adj = {}

    def __str__(self):
        res = ""
        for tail, headlist in self.adj.items():
            for head in headlist:
                res += f"({tail} -> {head})\t"
            res += "\n"
        return res
        
    def add_edge(self, tail, head):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append(head)

        if head not in self.adj:
            self.adj[head] = []

    def detect_cycle(self) -> bool:
        d = Deque()
        visited = set()
        indegree = {vertex : 0 for vertex in self.adj}

        # maintaining indegree dict
        for tail, headlist in self.adj.items():
            for head in headlist:
                indegree[head] += 1

        # indegree 0 add to queue
        for vertex in indegree:
            if indegree[vertex] == 0:
                d.enqueue(vertex)
                visited.add(vertex)

        if len(d.arr) == 0:
            return True 

        # applying bfs
        while len(d.arr):
            vertex = d.dequeue()
            for head in self.adj[vertex]:
                if head in visited:
                    return True
                else:
                    indegree[head] -= 1
                    if indegree[head] == 0:
                        d.enqueue(head)
                        visited.add(head)
        return False

if __name__ == "__main__":
    g = Graph()
    edges = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    print(g.detect_cycle())

"""
True
"""
