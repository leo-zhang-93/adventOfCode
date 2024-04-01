# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:35:57 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231217.txt'
grid = []
with open(path, 'r') as f:
    for line in f:
        grid.append(list(map(int, line[:-1])))

print(grid)

m, n = len(grid), len(grid[0])
print(m, n)

from collections import defaultdict
dic = defaultdict(int)
directions = {
    'u': [-1, 0], 
    'd': [1, 0], 
    'l': [0, -1], 
    'r': [0, 1],
    }

direction_changes = {
    'u': ['l', 'r'], 
    'd': ['l', 'r'], 
    'l': ['u', 'd'], 
    'r': ['u', 'd'], 
    }

seen = set()
## x, y, xd, yd, cumu, val, times
queue = [[0, 0, 0, 0, 0, grid[0][0], 0]]
tmp = []
cost = 1
seen.add(tuple(queue[0]))
while queue: 
    # print(queue[0], cost)
    x, y, xd, yd, cumu, val, times = queue.pop(0)
    if cumu == 0: 
        for dx, dy in directions.values(): 
            if not(xd + dx == 0 and yd + dy == 0) and 0 <= (x + dx) < m and 0 <= (y + dy) < n: 
                if times == 3 and xd == dx and yd == dy: 
                    continue
                newval = grid[x + dx][y + dy]
                if xd == dx and yd == dy: 
                    newtimes = times + 1
                else: 
                    newtimes = 1
                if (x + dx, y + dy, dx, dy, 0, newval, newtimes) not in seen: 
                    if newval == 1: 
                        seen.add((x + dx, y + dy, dx, dy, 0, newval, newtimes))
                        tmp.append([x + dx, y + dy, dx, dy, 0, newval, newtimes])
                    else: 
                        seen.add((x, y, dx, dy, 1, newval, newtimes))
                        tmp.append([x, y, dx, dy, 1, newval, newtimes])
    else: 
        if cumu + 1 < val: 
            seen.add((x, y, xd, yd, cumu + 1, val, times))
            tmp.append([x, y, xd, yd, cumu + 1, val, times])
        else: 
            seen.add((x + xd, y + yd, xd, yd, 0, val, times))
            tmp.append([x + xd, y + yd, xd, yd, 0, val, times])
            if x + xd == m - 1 and y + yd == n - 1: 
                print(cost)
                break
    if not queue: 
        queue = tmp
        tmp = []
        cost += 1
        print(cost)

            
        
    
            

