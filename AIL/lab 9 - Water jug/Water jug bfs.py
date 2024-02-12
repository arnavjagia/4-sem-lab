"""
Write a Python program to solve the water jug problem using Breadth First Search algorithm.

Problem: You are given two jugs, a 4-gallon one and a 3-gallon one.Neither has any
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
        res = "Queue: "
        for ele in self.arr:
            res += str(ele) + " "
        return res

def water_jug_bfs(x, y, goal):
    visited = set()
    path = []
    d = Deque([(0, 0)])

    while d.arr:
        a, b = d.dequeue()

        if goal in path:
            return True, path
        
        if (a, b) in visited:
            continue
        
        visited.add((a,b))
        path.append((a,b))

        # Fill jug A
        if a < x:
            d.enqueue((a, b))
        
        # Fill jug B
        if b < y:
            d.enqueue((a, y))
        
        # Empty jug A
        if a > 0:
            d.enqueue((0, b))
        
        # Empty jug B
        if b > 0:
            d.enqueue((a, 0))
        
        # Pour from A to B
        if a + b >= y:
            d.enqueue((a - (y - b), y))
        else:
            d.enqueue((0, a + b))
        
        # Pour from B to A
        if a + b >= x:
            d.enqueue((x, b - (x - a)))
        else:
            d.enqueue((a + b, 0))
    
    return False, path


x, y = 4, 3
goal = (2,0)

result, path = water_jug_bfs(x, y, goal)
if result:
    print(f'You can measure {goal} liters of water using {x}-liter and {y}-liter jugs.')
    print('Path to solution:')
    for step in path:
        print(step)
else:
    print(f'You cannot measure {goal} liters of water using {x}-liter and {y}-liter jugs.')