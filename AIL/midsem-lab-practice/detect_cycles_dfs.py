"""
Detect cycles - DFS
"""


class Stack:
    def __init__(self, arr: list = []):
        self.arr = arr

    def push(self, ele):
        self.arr.append(ele)

    def pop(self):
        return self.arr.pop() if self.arr else None

    def __str__(self) -> str:
        res = "Stack: "
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

    def detect_cycle(self, start_v) -> bool:
        visited = set()
        s = Stack()
        s.push(start_v)

        def util():
            vertex = s.pop()
            visited.add(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor in visited:
                    return True
                else:
                    s.push(neighbor)
                    if util() == True:
                        return True
            return False

        return util()


if __name__ == "__main__":
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for edge in edges:
        g.insert(edge[0], edge[1])
    print(g.detect_cycle(2))
