# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:00:01 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231214.txt'

ls = []
with open(path, 'r') as f:
    for line in f:
        ls.append(list(line[:-1]))

m, n = len(ls), len(ls[0])

res = 0
for j in range(n):
    currpos = 0
    for i in range(m):
        val = ls[i][j]
        if i == 0: 
            if val == '.': 
                currpos = 0
            elif val == '#': 
                currpos = 1
            else: 
                currpos = 1
                res += (m - i)
        else: 
            if val == '.': 
                continue
            elif val == '#': 
                currpos = i + 1
            else: 
                res += (m - currpos)
                currpos += 1   
                
print(res)

def move(grid, direction): 
    m, n = len(grid), len(grid[0])
    if direction == 'north': 
        for j in range(n):
            currpos = 0
            for i in range(m):
                val = grid[i][j]
                if i == 0: 
                    if val == '.': 
                        currpos = 0
                    elif val == '#': 
                        currpos = 1
                    else: 
                        currpos = 1
                else: 
                    if val == '.': 
                        continue
                    elif val == '#': 
                        currpos = i + 1
                    else: 
                        grid[currpos][j] = 'O'
                        if currpos != i: 
                            grid[i][j] = '.'
                        currpos += 1
        return grid
    elif direction == 'south': 
        newgrid = move(grid[::-1], 'north')
        return newgrid[::-1]
    elif direction == 'west': 
        for i in range(m):
            currpos = 0
            for j in range(n): 
                val = grid[i][j]
                if j == 0: 
                    if val == '.': 
                        currpos = 0
                    elif val == '#': 
                        currpos = 1
                    else: 
                        currpos = 1
                else: 
                    if val == '.': 
                        continue
                    elif val == '#': 
                        currpos = j + 1
                    else: 
                        grid[i][currpos] = 'O'
                        if currpos != j: 
                            grid[i][j] = '.'
                        currpos += 1
        return grid.copy()
    else: 
        newgrid = move([item[::-1] for item in grid], 'west')
        return [item[::-1] for item in newgrid]
    
ss = ''.join([''.join(item) for item in ls])
dic1 = {ss: 0}
dic2 = {0: ss}

i = 1
match = None
while True: 
    for direction in ['north', 'west', 'south', 'east']: 
        ls = move(ls, direction)
    newss = ''.join([''.join(item) for item in ls])
    if newss not in dic1: 
        dic1[newss] = i
        dic2[i] = newss
        i += 1
    else: 
        match = dic1[newss]
        break
print(match, i)

period = i - match
init = match
rounds = 1000000000
item = init + (rounds - init) % period
print(period, item)

txt = dic2[item]
result = 0
for i in range(m): 
    sub = txt[i * n: (i + 1) * n]
    result += sub.count('O') * (m - i)
print(result)

        
