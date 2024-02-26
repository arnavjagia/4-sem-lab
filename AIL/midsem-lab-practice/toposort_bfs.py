"""
Toposort - BFS
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

    def __str__(self) -> str:
        res = ""
        for vertex in self.adj:
            for neighbor in self.adj[vertex]:
                res += f"{vertex}->{neighbor}\t"
            res += "\n"
        return res

    def insert(self, tail, head):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append(head)

        if head not in self.adj:
            self.adj[head] = []

    def toposort_bfs(self) -> list:
        path = []
        visited = set()
        q = Queue()
        indegree = {vertex: 0 for vertex in self.adj}
        for vertex in self.adj:
            for neighbor in self.adj[vertex]:
                indegree[neighbor] += 1
        print(indegree)
        for vertex in self.adj:
            if indegree[vertex] == 0:
                q.enqueue(vertex)
        while q.arr:
            print(q)
            vertex = q.dequeue()
            visited.add(vertex)
            path.append(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.enqueue(neighbor)
        return path


if __name__ == "__main__":
    adj = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    g = Graph(adj)

    # g = Graph()
    # edges = [(5, 0), (4, 0), (5, 2), (2, 3), (3, 1), (4, 1)]
    # for edge in edges:
    #     g.insert(edge[0], edge[1])
    sort = g.toposort_bfs()
    print(sort)
