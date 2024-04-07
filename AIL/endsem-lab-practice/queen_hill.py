"""
n queens problem with hill climbing
"""

from random import randint, shuffle

class ChessBoard:
    def __init__(self, config=None, n=8):
        """
        `config` is a n sized array with column idx of queens in each row
        """

        if not config:
            config = [randint(0, n - 1) for i in range(n)]
        self.config = config.copy()
        self.n = n

    def __str__(self):
        res = "-" * 3 * self.n + "\n"
        for row in range(self.n):
            for col in range(self.n):
                if col == self.config[row]:
                    res += " Q "
                else:
                    res += " . "
            res += "\n"
        res += "-" * 3 * self.n
        res += f"\t Cost: {self.cost()}"
        return res

    def cost(self):
        cost = 0

        # col
        cost = self.n - len(set(self.config))
        for row in range(self.n):
            col = self.config[row]

            # diag
            for delta in range(1, self.n - row):
                if self.config[row + delta] in (col + delta, col - delta):
                    cost += 1

        return cost

    def neighbors(self):
        res = []

        for row in range(self.n):
            neighbor_config = self.config.copy()

            for col in range(self.n):
                if col != self.config[row]:
                    neighbor_config[row] = col
                    res.append(ChessBoard(neighbor_config, 8))

        shuffle(res)
        return res

def hill_climb(initial_state: ChessBoard) -> ChessBoard:
    x = initial_state
    print(x)
    while x.cost() != 0:
        x1 = min(x.neighbors(), key = lambda x: x.cost())
        print(x1)
        x = x1


if __name__ == "__main__":
    c = ChessBoard(n = 8)
    hill_climb(c)
