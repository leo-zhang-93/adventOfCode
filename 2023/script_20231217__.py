# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:11:36 2023

@author: Leo Zhang
"""
from collections import defaultdict
path = 'inputPartial_20231217.txt'
import copy
grid = []
with open(path, 'r') as f:
    for line in f:
        grid.append(list(map(int, line[:-1])))

# print(grid)

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

dir_pos = {
    'u': 0, 
    'l': 1, 
    'r': 2, 
    'd': 3,
    }

direction_changes = {
    'u': ['l', 'r'], 
    'd': ['l', 'r'], 
    'l': ['u', 'd'], 
    'r': ['u', 'd'], 
    }

seen = defaultdict(lambda: [[float('inf')] * 11 for _ in range(4)])
seen[(0, 0)] = [[0] * 11 for _ in range(4)]
for x in range(m): 
    for y in range(n): 
        for d in directions.keys(): 
            dx, dy = directions[d]
            idx = dir_pos[d]
            if 0 <= x + dx < m and 0 <= y + dy < n and not (x + dx == 0 and y + dy == 0): 
                for step in range(1, 11): 
                    seen[(x + dx, y + dy)][idx][step] = min(seen[(x + dx, y + dy)][idx][step], seen[(x, y)][idx][step - 1])
                    seen[(x + dx, y + dy)][idx][step] += grid[x + dx][y + dy]
                for newidx in range(4): 
                    if newidx == idx or newidx + idx == 3: 
                        continue
                    seen[(x + dx, y + dy)][idx][1] = min(seen[(x + dx, y + dy)][idx][1], min(seen[(x, y)][newidx][4:]))
                seen[(x + dx, y + dy)][idx][1] += grid[x + dx][y + dy]        
tmp_res = copy.deepcopy(seen[(m - 1, n - 1)])

cnt = 2
while True: 
    for x in range(m): 
        for y in range(n): 
            for d in directions.keys(): 
                dx, dy = directions[d]
                idx = dir_pos[d]
                if 0 <= x + dx < m and 0 <= y + dy < n and not (x + dx == 0 and y + dy == 0): 
                    for step in range(1, 11): 
                        seen[(x + dx, y + dy)][idx][step] = min(seen[(x + dx, y + dy)][idx][step], seen[(x, y)][idx][step - 1])
                        seen[(x + dx, y + dy)][idx][step] += grid[x + dx][y + dy]
                    for newidx in range(4): 
                        if newidx == idx or newidx + idx == 3: 
                            continue
                        seen[(x + dx, y + dy)][idx][1] = min(seen[(x + dx, y + dy)][idx][1], min(seen[(x, y)][newidx][4:]))
                    seen[(x + dx, y + dy)][idx][1] += grid[x + dx][y + dy]
    newres = copy.deepcopy(seen[m - 1, n - 1])
    print(cnt, newres)
    cnt += 1
    flag = 0
    for i in range(4): 
        for j in range(11): 
            if newres[i][j] != tmp_res[i][j]: 
                tmp_res = copy.deepcopy(newres)
                flag = 1
                break
            if flag == 1: 
                break
    if cnt == 100: 
        break
    

print(min([min(item) for item in newres]))