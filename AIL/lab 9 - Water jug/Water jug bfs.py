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
    d = Deque([(0, 0)])

    while d.arr:
        print(d)
        print(visited)
        a, b = d.dequeue()

        if goal in {a, b, a+b}:
            return True
        
        if (a, b) in visited:
            continue
        
        visited.add((a,b))

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
    
    return False


x, y = 4, 3
goal = 2

if water_jug_bfs(x, y, goal):
    print(f'You can measure {goal} liters of water using {x}-liter and {y}-liter jugs.')
else:
    print(f'You cannot measure {goal} liters of water using {x}-liter and {y}-liter jugs.')