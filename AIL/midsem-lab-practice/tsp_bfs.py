"""
TSP - BFS
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

    def bfs(self, start_v):
        q = Queue()
        q.enqueue((start_v, [start_v]))

        while q.arr:
            (vertex, path) = q.dequeue()
            for neighbor in set(self.adj[vertex]) - set(path):
                if len(path) + 1 == len(self.adj):
                    yield path + [neighbor]
                else:
                    q.enqueue((neighbor, path + [neighbor]))

    def tsp_bfs(self, start):
        shortest_path = None
        shortest_path_length = float("inf")

        for path in self.bfs(start):
            path_length = sum(self.adj[path[i - 1]][path[i]] for i in range(len(path)))
            if path_length < shortest_path_length:
                shortest_path_length = path_length
                shortest_path = path

        return shortest_path, shortest_path_length


if __name__ == "__main__":
    graph = {
        "A": {"B": 2, "C": 3, "D": 1},
        "B": {"A": 2, "C": 4, "D": 2},
        "C": {"A": 3, "B": 4, "D": 3},
        "D": {"A": 1, "B": 2, "C": 3},
    }
    g = Graph(graph)
    print(g.tsp_bfs("C"))
