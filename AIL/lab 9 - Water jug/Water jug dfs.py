"""
Write a Python program to solve the water jug problem using Depth First Search algorithm.

Problem: You are given two jugs, a 4-gallon one and a 3-gallon one.Neither has any
measuring mark on it.There is a pump that can be used to fill the jugs with water.How can
you get exactly 2 gallons of water into the 4-gallon jug.
"""

def water_jug_dfs(x, y, goal):
    visited = set()
    path = []
    s = [(0, 0)]

    while s:
        a, b = s.pop()

        if goal in path:
            return True, path
        
        if (a, b) in visited:
            continue
        
        visited.add((a,b))
        path.append((a,b))

        # Fill jug A
        if a < x:
            s.append((a, b))
        
        # Fill jug B
        if b < y:
            s.append((a, y))
        
        # Empty jug A
        if a > 0:
            s.append((0, b))
        
        # Empty jug B
        if b > 0:
            s.append((a, 0))
        
        # Pour from A to B
        if a + b >= y:
            s.append((a - (y - b), y))
        else:
            s.append((0, a + b))
        
        # Pour from B to A
        if a + b >= x:
            s.append((x, b - (x - a)))
        else:
            s.append((a + b, 0))
    
    return False, path


x, y = 4, 3
goal = (2,0)

result, path = water_jug_dfs(x, y, goal)
if result:
    print(f'You can measure {goal} liters of water using {x}-liter and {y}-liter jugs.')
    print('Path to solution:')
    for step in path:
        print(step)
else:
    print(f'You cannot measure {goal} liters of water using {x}-liter and {y}-liter jugs.')