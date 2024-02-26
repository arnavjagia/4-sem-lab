"""
bfs algo for graph
"""


class Queue:
    def __init__(self, arr: list = []):
        self.arr = arr

    def enqueue(self, ele):
        self.arr.append(ele)

    def dequeue(self):
        return self.arr.pop(0) if self.arr else None

    def __str__(self) -> str:
        res = "Queue: "
        for ele in self.arr:
            res += f"{ele} "
        return res


class Graph:
    def __init__(self, adj: dict = {}):
        self.adj = adj

    def insert(self, tail, head):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append(head)

        if head not in self.adj:
            self.adj[head] = []

    def __str__(self) -> str:
        res = ""
        for vertex in self.adj:
            for neighbor in vertex:
                res += f"{vertex}->{neighbor}\t"
            res += "\n"
        return res

    def bfs(self, start_v):
        path = []
        visited = set()
        q = Queue()
        q.enqueue(start_v)
        while q.arr:
            vertex = q.dequeue()
            visited.add(vertex)
            path.append(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    q.enqueue(neighbor)
        return path


if __name__ == "__main__":

    adj = {0: [2, 3, 1], 1: [0], 2: [0, 4], 3: [0], 4: [2]}
    adj = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7: []}
    g = Graph(adj)
    path = g.bfs(1)
    print(path)
