# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:49:53 2023

@author: Leo Zhang
"""

from collections import defaultdict
path = 'inputPartial_20231223.txt'
grid = []
with open(path, 'r') as f:
    for line in f:
        grid.append(list(line[:-1]))

m, n = len(grid), len(grid[0])
starty = grid[0].index('.')
endy = grid[-1].index('.')

# print(m, n, starty, endy)
grid_status = [[0] * n for _ in range(m)]
directions = [
    [-1, 0], 
    [1, 0], 
    [0, 1], 
    [0, -1]
    ]

def calc1(x, y): 
    # print(x, y)
    if x == m - 1 and y == endy: 
        return 0
    else: 
        grid_status[x][y] = 1
        res = -float('inf')
        if grid[x][y] in '.':
            for dx, dy in directions: 
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] != '#' and grid_status[x + dx][y + dy] == 0: 
                    res = max(res, 1 + calc1(x + dx, y + dy))
        else: 
            if False: 
                pass
            if grid[x][y] == '>': 
                idx = 2
            elif grid[x][y] == '^': 
                idx = 0
            elif grid[x][y] == 'v': 
                idx = 1
            elif grid[x][y] == '<': 
                idx = 3
            dx, dy = directions[idx]
            if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] != '#' and grid_status[x + dx][y + dy] == 0: 
                res = max(res, 1 + calc1(x + dx, y + dy))
        grid_status[x][y] = 0
        return res
        
# print(calc1(0, starty))

# print(calc1(m - 2, n - 2))
# print(calc1(m - 2, n - 4))

# grid_status2 = [[0] * n for _ in range(m)]  
# def calc2(x, y): 
#     if x == m - 1 and y == endy: 
#         return 0
#     else: 
#         grid_status2[x][y] = 1
#         res = -float('inf')
#         for dx, dy in directions: 
#             if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] != '#' and grid_status2[x + dx][y + dy] == 0: 
#                 res = max(res, 1 + calc2(x + dx, y + dy))
#         grid_status2[x][y] = 0
#         return res

# print(calc2(0, starty))

ls_intersection = []
for i in range(m): 
    for j in range(n): 
        if grid[i][j] == '.': 
            cnt = 0
            for dx, dy in directions: 
                if 0 <= i + dx < m and 0 <= j + dy < n: 
                    if grid[i + dx][j + dy] in '<>^v': 
                        cnt += 1
            if cnt >= 3: 
                ls_intersection.append([i, j])
ls_intersection.append([0, starty])
ls_intersection.append([m - 1, endy])

print(len(ls_intersection))
st_intersection = set([tuple(item) for item in ls_intersection])

# print(st_intersection)

seen = set()
def goThru(x, y): 
    queue = [[x, y]]
    cnt = 1
    tmp_seen = set()
    while queue: 
        x0, y0 = queue.pop(0)
        seen.add((x0, y0))
        for dx, dy in directions: 
            if 0 <= x0 + dx < m and 0 <= y0 + dy < n and grid[x0 + dx][y0 + dy] != '#' and (x0 + dx, y0 + dy) not in seen and (x0 + dx, y0 + dy) not in tmp_seen: 
                cnt += 1
                queue.append([x0 + dx, y0 + dy])
                tmp_seen.add((x0 + dx, y0 + dy))
                if (x0 + dx, y0 + dy) in st_intersection: 
                    return (x0 + dx, y0 + dy), cnt
    return (None, None), 0
                
dic_distance = defaultdict(dict)
for x, y in ls_intersection: 
    seen.add((x, y))
    for dx, dy in directions: 
        newx = x + dx
        newy = y + dy
        if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] != '#' and (newx, newy) not in seen: 
            (x1, y1), cnt = goThru(newx, newy)
            if x1 is not None: 
                dic_distance[(x, y)][(x1, y1)] = cnt
                dic_distance[(x1, y1)][(x, y)] = cnt

status_dic = {key: 0 for key in dic_distance}

def calcDis(x, y): 
    print(x, y)
    if x == m - 1 and y == endy: 
        # print(3, x, y, 0)
        return 0
    else: 
        if (m - 1, endy) in dic_distance[(x, y)]: 
            res = dic_distance[(x, y)][(m - 1, endy)]
            # print(2, x, y, res)
            return res
        else: 
            status_dic[(x, y)] = 1
            res = -float('inf')
            for newkey in dic_distance[(x, y)]: 
                if status_dic[newkey] == 0: 
                    res = max(res, dic_distance[(x, y)][newkey] + calcDis(*newkey))
            status_dic[(x, y)] = 0
            # print(1, x, y, res)
            return res
        
print(calcDis(0, starty))
                



                        