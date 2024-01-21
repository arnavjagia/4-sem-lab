# to keep track of the blocks of maze
class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# each block will have its own position and cost of steps taken
class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost

def create_node(x, y, c):
    val = Grid_Position(x, y)
    return Node(val, c + 1)

#dfs algo for maze
def dfs(Grid, dest: Grid_Position, start: Grid_Position):
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]
    m, n = (len(Grid), len(Grid))
    visited_blocks = [[False for i in range(m)]
               for j in range(n)]
    visited_blocks[start.x][start.y] = True
    stack = []
    sol = Node(start, 0)
    stack.append(sol)
    neigh = 4
    cost = 0
    while stack:
        current_block = stack.pop()
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Path found!!")
            print("Total nodes visited = ", cost)
            return current_block.cost
        x_pos = current_pos.x
        y_pos = current_pos.y
     
        for i in range(neigh):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos != 4 and x_pos != -1 and y_pos != 4 and y_pos != -1:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack.append(create_node(x_pos, y_pos, current_block.cost))
    return -1
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maze = [[0, 1, 0, 1],
            [1, 1, 1, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1]]
    destination = Grid_Position(1, 0)
    starting_position = Grid_Position(3, 3)

    res2 = dfs(maze, destination, starting_position)
    if res2 != -1:
        print("Steps with backtracking = ", res2)
    else:
        print("Path does not exit")

"""
Path found!!
Total nodes visited =  54
Steps with backtracking =  29

References:
https://github.com/Areesha-Tahir/BFS-DFS-Maze-Solver-In-Python/blob/main/main.py
"""