class Stack:
    def __init__(self, arr: list = []):
        self.arr = arr

    def push(self, ele):
        self.arr.append(ele)

    def pop(self):
        return self.arr.pop()

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
                res += f"({vertex}->{neighbor})\t"
            res += "\n"
        return res

    # def __dfs_util(self, path, visited, stack):
    #     vertex = stack.pop()
    #     visited.add(vertex)
    #     path.append(vertex)
    #     for neighbor in self.adj[vertex]:
    #         if neighbor not in visited:
    #             stack.push(neighbor)
    #             self.__dfs_util(path, visited, stack)

    # def dfs(self, start_v) -> list:
    #     "returns dfs path"
    #     path = []
    #     visited = set()
    #     stack = Stack()
    #     stack.push(start_v)
    #     self.__dfs_util(path, visited, stack)
    #     return path

    def dfs(self, start_v) -> list:
        path = []
        visited = set()
        s = Stack()
        s.push(start_v)

        def util():
            vertex = s.pop()
            visited.add(vertex)
            path.append(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    s.push(neighbor)
                    util()

        util()
        return path


if __name__ == "__main__":

    adj = {0: [2, 3, 1], 1: [0], 2: [0, 4], 3: [0], 4: [2]}
    adj = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7: []}
    g = Graph(adj)
    path = g.dfs(1)
    print(path)