"""
bfs algo implemented 

aditya mohan - 3 labs miss
"""

class Dequeue:
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
    def __str__(self):
        res = ""
        for tail, headlist in self.adj.items():
            for head in headlist:
                res += f"({tail} -> {head})\t"
            res += "\n"
        return res
        
    def __init__(self):
        self.adj = {}
        
    def add_edge(self, tail, head):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append(head)                    

if __name__ == "__main__":
    d = Dequeue()
    print(d)
    d.enqueue(1)
    print(d)
    d.enqueue(2)
    print(d)
    g = Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    print(g)
