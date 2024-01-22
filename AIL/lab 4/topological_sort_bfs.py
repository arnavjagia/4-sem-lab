"""
Implement topological sorting using BFS algorithm for the following graph.
https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/
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

    def topo_sort_bfs(self) -> list:
        T = []
        d = Deque()
        visited = [0 for vertex in self.adj]
        indegree = {vertex : 0 for vertex in self.adj}

        # maintaining indegree dict
        for tail, headlist in self.adj.items():
            for head in headlist:
                indegree[head] += 1

        # indegree 0 add to queue
        for vertex in indegree:
            if indegree[vertex] == 0:
                d.enqueue(vertex)
                visited[vertex] = True

        # applying bfs
        while d:
            vertex = d.dequeue()
            T.append(vertex)
            for head in self.adj[vertex]:
                if not visited[head]: # not necessary
                    indegree[head] -= 1
                    if indegree[head] == 0:
                        d.enqueue(head)
                        visited[head] = True
        return T
                

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
    g.topo_sort_bfs()
    print(g.visited)
