# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:53:07 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231210.txt'
# path = 'inputPartial_20231210_.txt'

mat = []
i = 0
xs = None
ys = None
with open(path, 'r') as f:
    for line in f:
        tmp_ls = list(line[:-1])
        if 'S' in line: 
            xs = i
            ys = tmp_ls.index('S')
        mat.append(tmp_ls)
        i += 1

m, n = len(mat), len(mat[0])
print(m, n)

directions = ['U', 'D', 'L','R']
res = []

# L
newx = xs
newy = ys - 1
if newy >= 0 and mat[newx][newy] in ['-', 'L', 'F']: 
    res.append('L')

# R
newx = xs
newy = ys + 1
if newy <= n - 1 and mat[newx][newy] in ['-', 'J', 'T']: 
    res.append('R')
    
# U
newx = xs - 1
newy = ys
if newx >= 0 and mat[newx][newy] in ['|', '7', 'F']: 
    res.append('U')
    
# U
newx = xs + 1
newy = ys
if newx <= m and mat[newx][newy] in ['|', 'L', 'J']: 
    res.append('D')

if 'L' in res: 
    prevpos = [xs, ys]
    pos = [xs, ys - 1]
    i = 1

seen_loop = set([tuple(pos), (xs, ys)])

# shows the direction of inner
dic = {(xs, ys): [1, -1]}
deg = 0

while True: 
    x, y = pos
    prevx, prevy = prevpos
    val = mat[x][y]
    if val == '|': 
        if x == prevx + 1:
            pos = [x + 1, y]
            dic[(x, y)] = [[0, 1]]
        else: 
            pos = [x - 1, y]
            dic[(x, y)] = [[0, -1]]
    elif val == '-': 
        if y == prevy + 1: 
            pos = [x, y + 1]
            dic[(x, y)] = [[-1, 0]]
        else: 
            pos = [x, y - 1]
            dic[(x, y)] = [[1, 0]]
    elif val == 'L': 
        if y == prevy - 1: 
            pos = [x - 1, y]
            deg -= 90
            dic[(x, y)] = [[1, -1], [0, -1], [1, 0]]
        else:
            pos = [x, y + 1]
            deg += 90
            dic[tuple(pos)] = [[-1, 1]]
    elif val == 'J': 
        if y == prevy + 1: 
            pos = [x - 1, y]
            deg += 90
            dic[(x, y)] = [[-1, -1]]
        else: 
            pos = [x, y - 1]
            deg -= 90
            dic[(x, y)] = [[1, 0], [1, 1], [0, 1]]
    elif val == '7': 
        if y == prevy + 1: 
            pos = [x + 1, y]
            deg -= 90
            dic[(x, y)] = [[-1, 0], [-1, 1], [0, 1]]
        else: 
            pos = [x, y - 1]
            deg += 90
            dic[(x, y)] = [[1, -1]]
    elif val == 'F': 
        if y == prevy - 1: 
            pos = [x + 1, y]
            deg += 90
            dic[(x, y)] = [[1, 1]]
        else: 
            pos = [x, y + 1]
            deg -= 90
            dic[(x, y)] = [[0, -1], [-1, -1], [-1, 0]]
    seen_loop.add((x, y))
    prevpos = [x, y]
    i += 1
    if pos == [xs, ys]: 
        deg += 90
        break
print(i)
print(deg)

seen = set()
dirs = [
        [-1, 0], 
        [1, 0], 
        [0, -1], 
        [0, 1],
        ]

dirs1 = [
    [-1, -1], 
    [-1, 1], 
    [1, -1], 
    [1, 1]
    ]

# print(dic)
res = 0
for i in range(m): 
    for j in range(n): 
        if (i, j) in seen or (i, j) in seen_loop: 
            continue
        flag = False
        cnt = 1
        queue = [[i, j]]
        seen.add((i, j))
        while queue: 
            x, y = queue.pop(0)
            for dx, dy in dirs: 
                newx = x + dx
                newy = y + dy
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen and (newx, newy) not in seen_loop: 
                    seen.add((newx, newy))
                    queue.append([newx, newy])
                    cnt += 1
            for dx1, dy1 in dirs + dirs1: 
                newx1 = x + dx1
                newy1 = y + dy1
                if (newx1, newy1) in dic: 
                    for a, b in dic[(newx1, newy1)]:
                        if dx1 + a == 0 and dy1 + b == 0: 
                            # print(x, y, newx1, newy1, mat[newx1][newy1], dx1, dy1, dic[(newx1, newy1)])
                            flag = True
        if flag == True: 
            res += cnt
        print(i, j, cnt, flag)

print(res)
                
        
        
    
            

    