# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:52:14 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231216_.txt'
grid = []
with open(path, 'r') as f:
    for line in f:
        grid.append(line[:-1])

m, n = len(grid), len(grid[0])

x = 0
y = 0
seen = set([(x, y)])
seenall = set([(x, y, 'r')])
queue = [(x, y, 'r')]

directions = {
    'u': [-1, 0], 
    'd': [1, 0], 
    'l': [0, -1], 
    'r': [0, 1]
    }

while queue: 
    x0, y0, direction = queue.pop()
    newdirection = None
    if grid[x0][y0] == '.': 
        newdirection = direction
    elif grid[x0][y0] == '\\':
        if direction == 'r': 
            newdirection = 'd'
        elif direction == 'd': 
            newdirection = 'r'
        elif direction == 'l': 
            newdirection = 'u'
        else: 
            newdirection = 'l'
    elif grid[x0][y0] == '/': 
        if direction == 'r': 
            newdirection = 'u'
        elif direction == 'd': 
            newdirection = 'l'
        elif direction == 'l': 
            newdirection = 'd'
        else: 
            newdirection = 'r'
    elif grid[x0][y0] == '|': 
        if direction in 'ud': 
            newdirection = direction
        else: 
            newdirection = 'ud'
    else: 
        if direction in 'lr': 
            newdirection = direction
        else: 
            newdirection = 'lr'
    # print(x0, y0, grid[x0][y0], direction, newdirection)
    for newdir in newdirection: 
        dx, dy = directions[newdir]
        x1 = x0 + dx 
        y1 = y0 + dy
        if 0 <= x1 < m and 0 <= y1 < n and (x1, y1, newdir) not in seenall: 
            seenall.add((x1, y1, newdir))
            queue.append((x1, y1, newdir))
            seen.add((x1, y1))

print(len(seen))


def calc(initx, inity, initd): 
    seen = set([(initx, inity)])
    seenall = set([(initx, inity, initd)])
    queue = [(initx, inity, initd)]
    
    directions = {
        'u': [-1, 0], 
        'd': [1, 0], 
        'l': [0, -1], 
        'r': [0, 1]
        }
    
    while queue: 
        x0, y0, direction = queue.pop()
        newdirection = None
        if grid[x0][y0] == '.': 
            newdirection = direction
        elif grid[x0][y0] == '\\':
            if direction == 'r': 
                newdirection = 'd'
            elif direction == 'd': 
                newdirection = 'r'
            elif direction == 'l': 
                newdirection = 'u'
            else: 
                newdirection = 'l'
        elif grid[x0][y0] == '/': 
            if direction == 'r': 
                newdirection = 'u'
            elif direction == 'd': 
                newdirection = 'l'
            elif direction == 'l': 
                newdirection = 'd'
            else: 
                newdirection = 'r'
        elif grid[x0][y0] == '|': 
            if direction in 'ud': 
                newdirection = direction
            else: 
                newdirection = 'ud'
        else: 
            if direction in 'lr': 
                newdirection = direction
            else: 
                newdirection = 'lr'
        # print(x0, y0, grid[x0][y0], direction, newdirection)
        for newdir in newdirection: 
            dx, dy = directions[newdir]
            x1 = x0 + dx 
            y1 = y0 + dy
            if 0 <= x1 < m and 0 <= y1 < n and (x1, y1, newdir) not in seenall: 
                seenall.add((x1, y1, newdir))
                queue.append((x1, y1, newdir))
                seen.add((x1, y1))
    
    return len(seen)

result = 0
for j in range(n): 
    result = max(result, calc(0, j, 'd'))
    result = max(result, calc(m - 1, j, 'u'))
    
for i in range(m): 
    result = max(result, calc(i, 0, 'r'))
    result = max(result, calc(i, n - 1, 'l'))

print(result)
        