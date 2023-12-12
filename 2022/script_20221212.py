# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:20:01 2022

@author: Leo Zhang
"""

path = 'inputPartial_20221212.txt'

def part1(path):
    
    grid = []
    with open(path, 'r') as f:
        for line in f: 
            grid.append(list(line[:-1]))
    
    m, n = len(grid), len(grid[0])
    for i in range(m): 
        for j in range(n): 
            if grid[i][j] == 'S': 
                grid[i][j] = 'a'
                start = [i, j]
            if grid[i][j] == 'E': 
                grid[i][j] = 'z'
                end = [i, j]
    
    queue = [start]
    tmp = []
    steps = 1
    seen = set([(*start)])
    directions = [
        [0, 1], 
        [0, -1], 
        [1, 0], 
        [-1, 0], 
        ]
    
    while queue: 
        x, y = queue.pop(0)
        for dx, dy in directions: 
            newx = x + dx
            newy = y + dy
            if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen and ord(grid[newx][newy]) - ord(grid[x][y]) <= 1: 
                if newx == end[0] and newy == end[1]: 
                    return steps
                else: 
                    tmp.append([newx, newy])
                    seen.add((newx, newy))
        if not queue: 
            queue = tmp
            tmp = []
            steps += 1
            
def part2(path):
    
    grid = []
    with open(path, 'r') as f:
        for line in f: 
            grid.append(list(line[:-1]))
    
    m, n = len(grid), len(grid[0])
    for i in range(m): 
        for j in range(n): 
            if grid[i][j] == 'S': 
                grid[i][j] = 'a'
                start = [i, j]
            if grid[i][j] == 'E': 
                grid[i][j] = 'z'
                end = [i, j]
    
    queue = [end]
    tmp = []
    steps = 1
    seen = set([(*start)])
    directions = [
        [0, 1], 
        [0, -1], 
        [1, 0], 
        [-1, 0], 
        ]
    
    while queue: 
        x, y = queue.pop(0)
        for dx, dy in directions: 
            newx = x + dx
            newy = y + dy
            if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen and ord(grid[x][y]) - ord(grid[newx][newy]) <= 1: 
                if grid[newx][newy] == 'a':  
                    return steps
                else: 
                    tmp.append([newx, newy])
                    seen.add((newx, newy))
        if not queue: 
            queue = tmp
            tmp = []
            steps += 1
            
path1 = 'inputPartial_20221212.txt'
path2 = 'inputFull_20221212.txt'

print(part1(path1))
print(part1(path2))
print(part2(path1))
print(part2(path2))
            
                
    
