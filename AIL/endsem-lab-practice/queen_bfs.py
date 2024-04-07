"""
n queens problem using bfs
"""

from __future__ import annotations

from random import randint, shuffle


class ChessBoard:
    def __init__(self, config=None, n=8):
        if not config:
            config = [randint(0, n - 1) for _ in range(n)]
        self.config = config.copy()
        self.n = n

    def __str__(self):
        res = "-" * 3 * self.n + "\n"
        for row in range(self.n):
            for col in range(self.n):
                res += " Q " if self.config[row] == col else " . "
            res += "\n"
        res += "-" * 3 * self.n
        res += f"\t Cost = {self.cost()}"
        return res

    def cost(self):
        # col and diag
        cost = self.n - len(set(self.config))

        for row in range(self.n):
            col = self.config[row]

            for delta in range(1, self.n - row):
                if self.config[row + delta] in (col + delta, col - delta):
                    cost += 1

        return cost

    def neighbors(self) -> list:
        q = []
        for row in range(self.n):
            neighbor_config = self.config.copy()
            for col in range(self.n):
                if self.config[row] != col:
                    neighbor_config[row] = col
                    if ChessBoard(neighbor_config, self.n).cost() < self.cost():
                        q.append(ChessBoard(neighbor_config, self.n))
        shuffle(q)
        return q


def bfs_queens(initial_config: ChessBoard):
    q = [initial_config]
    visited = set()
    while q:
        curr = q.pop(0)
        if curr in visited:
            continue
        if curr.cost() == 0:
            return curr
        visited.add(curr)
        q.extend(curr.neighbors())
    return curr


if __name__ == "__main__":
    c = ChessBoard(n=10)
    while c.cost() >= 7:
        c = ChessBoard(n=10)
    print(c)
    print(bfs_queens(c))
