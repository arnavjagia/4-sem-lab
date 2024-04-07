"""
You are given two jugs, a 4-gallon one and a 3-gallon one.Neither has any 
measuring mark on it.There is a pump that can be used to fill the jugs with water.How can 
you get exactly 2 gallons of water into the 4-gallon jug.
"""


class Deque:
    def __init__(self, init: list = []):
        self.arr = init

    def enqueue(self, ele):
        self.arr.append(ele)

    def dequeue(self):
        return self.arr.pop(0)

    def __str__(self):
        res = "Queue:\t"
        for ele in self.arr:
            res += f"{ele}\t"
        return res + "\n"


class Jugs:
    def __init__(self, a: int = 0, b: int = 0):
        """
        `a` and `b` are the max capacity of jug 1 and jug 2 resp.\\
        `x` and `y` is water in jug 1 and jug 2 resp.
        """
        self.a = a
        self.b = b

    def pour_jugs(self, init_config: tuple, goal: tuple) -> list[tuple]:
        """
        `returns` path to final config \\
        `res_a` water in jug a \\
        `res_b` water in jug b
        """
        path = []
        visited = set()
        q = Deque([init_config])
        while q.arr:
            print(q)
            cur_config = q.dequeue()
            if cur_config in visited:
                continue
            visited.add(cur_config)
            x, y = cur_config

            if (x, y) == (0, 2):
                (x, y) = (2, 0)
            if (x, y) is goal:
                return path
            if x < self.a:
                q.enqueue((self.a, y))
            if y < self.b:
                q.enqueue((x, self.b))
            if x > 0:
                q.enqueue((0, y))
            if y > 0:
                q.enqueue((x, 0))
            if x + y >= self.a and y > 0:
                q.enqueue((self.a, y - (self.a - x)))
            if x + y >= self.b and x > 0:
                q.enqueue((x - (self.b - y), self.b))
            if x + y <= self.a and y > 0:
                q.enqueue((x + y, 0))
            if x + y <= self.b and x > 0:
                q.enqueue((0, x + y))

        return path


if __name__ == "__main__":
    j = Jugs(4, 3)
    print(j.pour_jugs((0, 0), (2, 0)))
