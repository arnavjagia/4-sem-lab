"""
Topological sort - DFS
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

    def insert(self, tail, head):
        if tail not in self.adj:
            self.adj[tail] = []
        self.adj[tail].append(head)

        if head not in self.adj:
            self.adj[head] = []

    def __str__(self) -> str:
        res = ""
        for vertex in self.adj:
            for neighbor in self.adj[vertex]:
                res += f"{vertex}->{neighbor}\t"
            res += "\n"
        return res

    def toposort_dfs(self):
        path = []
        visited = set()
        s = Stack()
        indegree = {vertex: 0 for vertex in self.adj}
        for vertex in self.adj:
            for neighbor in self.adj[vertex]:
                indegree[neighbor] += 1
        for vertex in self.adj:
            if indegree[vertex] == 0:
                s.push(vertex)

        def util():
            if not s.arr:
                return
            print(s)  # prints stack
            vertex = s.pop()
            visited.add(vertex)
            path.append(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        s.push(neighbor)
                    util()

        util()
        return path


if __name__ == "__main__":
    adj = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    g = Graph(adj)

    # g = Graph()
    # edges = [(5, 0), (4, 0), (5, 2), (2, 3), (3, 1), (4, 1)]
    # for edge in edges:
    #     g.insert(edge[0], edge[1])
    sort = g.toposort_dfs()
    print(sort)

    # Test for edge cases
    # g_empty = Graph()
    # print(g_empty.toposort_dfs())
    # g_single_vertex = Graph({0: []})
    # print(g_single_vertex.toposort_dfs())
    # g_disconnected = Graph({0: [1], 1: [2], 2: [], 3: []})
    # print(g_disconnected.toposort_dfs())
    # g_cyclic = Graph({0: [1], 1: [2], 2: [0]})
    # print(g_cyclic.toposort_dfs())
