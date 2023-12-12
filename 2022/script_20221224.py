# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 22:49:17 2023

@author: Leo Zhang
"""
path = 'inputFull_20221224.txt'

n = None
ls = []
with open(path, 'r') as f:
    for line in f: 
        ls.append(line[1:-2])
ls = ls[1:-1]
m, n = len(ls), len(ls[0])
track4 = [set() for _ in range(4)]

for i in range(m): 
    for j in range(n): 
        val = ls[i][j]
        if val == "^":
            track4[0].add((i, j))
        elif val == 'v': 
            track4[1].add((i, j))
        elif val == '<': 
            track4[2].add((i, j))
        elif val == '>': 
            track4[3].add((i, j))
print([len(item) for item in track4])

def move(): 
    for i in range(4): 
        tmp = set()
        for x, y in track4[i]: 
            if i == 0: 
                if x == 0: 
                    tmp.add((m - 1, y))
                else: 
                    tmp.add((x - 1, y))
            elif i == 1: 
                if x == m - 1: 
                    tmp.add((0, y))
                else: 
                    tmp.add((x + 1, y))
            elif i == 2: 
                if y == 0: 
                    tmp.add((x, n - 1))
                else: 
                    tmp.add((x, y - 1))
            else: 
                if y == n - 1: 
                    tmp.add((x, 0))
                else: 
                    tmp.add((x, y + 1))
        track4[i] = tmp

directions = [
    [0, -1], 
    [0, 1],
    [-1, 0], 
    [1, 0],
    [0, 0],
    ]

CONSTANT = m * n
all_res = 0

level = 0
while any([(0, 0) in item for item in track4]): 
    move()
    level += 1
queue = [[0, 0]]
tmp = []

seen = set(([0, 0, level]))
result = 0

while queue: 
    x, y = queue.pop(0)
    for dx, dy in directions: 
        newx = x + dx
        newy = y + dy
        flag = 0
        flag1 = 0
        if 0 <= newx <= m - 1 and 0 <= newy <= n - 1 and all([(newx, newy) not in item for item in track4]) and (newx, newy, level) not in seen:
            if newx == m - 1 and newy == n - 1: 
                flag = 1
                result = level + 1
            tmp.append((newx, newy))
            seen.add((newx, newy, level))
        if flag == 1: 
            break
    if flag == 1: 
        break
    if not queue: 
        queue = tmp
        tmp = []
        move()
        level += 1

print(result)
# print()
move()
level += 1
move()
level += 1

queue = [[m, n - 1]]
tmp = []
# print(level, track4)

while queue: 
    x, y = queue.pop(0)
    # print(x, y, queue, level)
    for dx, dy in directions: 
        newx = x + dx
        newy = y + dy
        flag = 0
        if (newx == m and newy == n - 1 and (newx, newy, level) not in seen) or (0 <= newx <= m - 1 and 0 <= newy <= n - 1 and all([(newx, newy) not in item for item in track4]) and (newx, newy, level) not in seen):
            if newx == 0 and newy == 0: 
                flag = 1
                result = level + 1
            tmp.append((newx, newy))
            seen.add((newx, newy, level))
        if flag == 1: 
            break
    if flag == 1: 
        break
    if not queue: 
        # print(queue, tmp)
        queue = tmp
        tmp = []
        move()
        level += 1
        # print(level, track4)

print(result)
move()
level += 1
move()
level += 1

queue = [[-1, 0]]
tmp = []

while queue: 
    x, y = queue.pop(0)
    for dx, dy in directions: 
        newx = x + dx
        newy = y + dy
        flag = 0
        if (newx == -1 and newy == 0 and (newx, newy, level) not in seen) or (0 <= newx <= m - 1 and 0 <= newy <= n - 1 and all([(newx, newy) not in item for item in track4]) and (newx, newy, level) not in seen):
            if newx == m - 1 and newy == n - 1: 
                flag = 1
                result = level + 1
            tmp.append((newx, newy))
            seen.add((newx, newy, level))
        if flag == 1: 
            break
    if flag == 1: 
        break
    if not queue: 
        # print(queue, tmp)
        queue = tmp
        tmp = []
        move()
        level += 1

print(result)
            
        
        