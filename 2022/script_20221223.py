# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:42:35 2022

@author: Leo Zhang
"""

def part1(path):
    
    from collections import defaultdict
    
    ls = []
    with open(path, 'r') as f:
        for line in f:
            ls.append(line[:-1])
    
    m, n = len(ls), len(ls[0])
    st = set()
    for i in range(m): 
        for j in range(n): 
            if ls[i][j] == '#': 
                st.add((i, j))
    
    # print(sorted(st))
    
    posN = [
            [-1, -1], 
            [-1, 0], 
            [-1, 1], 
            ]
    
    posS = [
            [1, -1], 
            [1, 0], 
            [1, 1], 
            ]
    
    posW = [
            [-1, -1], 
            [0, -1], 
            [1, -1], 
            ]
    
    posE = [
            [-1, 1], 
            [0, 1], 
            [1, 1],
            ]
    
    dic_poss = {
        'N': posN, 
        'S': posS, 
        'W': posW, 
        'E': posE, 
        }
    
    dic_moves = {
        'X': [0, 0], 
        'N': [-1, 0], 
        'S': [1, 0], 
        'W': [0, -1], 
        'E': [0, 1], 
        }
    
    ls_turns = 'NSWENSW'
    
    for i in range(10): 
        i %= 4
        directions = ls_turns[i:i + 4]
        dic = defaultdict(list)
        for x, y in st:
            flag0 = 0
            flag_assgin = 0
            target_dir = 'X'
            for direction in directions:
                pos = dic_poss[direction]
                flag1 = 0
                for dx, dy in pos: 
                    newx = x + dx
                    newy = y + dy
                    if (newx, newy) in st: 
                        flag1 = 1
                        flag0 = 1
                        continue
                if flag1 == 0 and flag_assgin == 0: 
                    flag_assgin = 1
                    target_dir = direction
            if flag0 == 0: 
                target_dir = 'X'
            dxx, dyy = dic_moves[target_dir]
            xx = x + dxx
            yy = y + dyy
            dic[(xx, yy)].append((x, y))
        st = set()
        for key in dic.keys(): 
            xx, yy = key
            if len(dic[key]) == 1: 
                st.add(key)
            else: 
                for item in dic[key]: 
                    st.add(item)
    
    # print(st)
    l = float('inf')
    r = -float('inf')
    u = float('inf')
    d = -float('inf')
    
    for x, y in st:
        l = min(l, x)
        r = max(r, x)
        u = min(u, y)
        d = max(d, y)
    
    return (d - u + 1) * (r - l + 1) - len(st)

def part2(path):
    
    from collections import defaultdict
    
    ls = []
    with open(path, 'r') as f:
        for line in f:
            ls.append(line[:-1])
    
    m, n = len(ls), len(ls[0])
    st = set()
    for i in range(m): 
        for j in range(n): 
            if ls[i][j] == '#': 
                st.add((i, j))
    
    # print(sorted(st))
    
    posN = [
            [-1, -1], 
            [-1, 0], 
            [-1, 1], 
            ]
    
    posS = [
            [1, -1], 
            [1, 0], 
            [1, 1], 
            ]
    
    posW = [
            [-1, -1], 
            [0, -1], 
            [1, -1], 
            ]
    
    posE = [
            [-1, 1], 
            [0, 1], 
            [1, 1],
            ]
    
    dic_poss = {
        'N': posN, 
        'S': posS, 
        'W': posW, 
        'E': posE, 
        }
    
    dic_moves = {
        'X': [0, 0], 
        'N': [-1, 0], 
        'S': [1, 0], 
        'W': [0, -1], 
        'E': [0, 1], 
        }
    
    ls_turns = 'NSWENSW'
    
    ii = 0
    while True: 
        i = ii % 4
        directions = ls_turns[i:i + 4]
        dic = defaultdict(list)
        total_flag = 0
        for x, y in st:
            flag0 = 0
            flag_assgin = 0
            target_dir = 'X'
            for direction in directions:
                pos = dic_poss[direction]
                flag1 = 0
                for dx, dy in pos: 
                    newx = x + dx
                    newy = y + dy
                    if (newx, newy) in st: 
                        flag1 = 1
                        flag0 = 1
                        continue
                if flag1 == 0 and flag_assgin == 0: 
                    flag_assgin = 1
                    target_dir = direction
            if flag0 == 0: 
                target_dir = 'X'
            else: 
                # print(i, x, y)
                total_flag = 1
            dxx, dyy = dic_moves[target_dir]
            xx = x + dxx
            yy = y + dyy
            dic[(xx, yy)].append((x, y))
        if total_flag == 0: 
            break
        st = set()
        for key in dic.keys(): 
            xx, yy = key
            if len(dic[key]) == 1: 
                st.add(key)
            else: 
                for item in dic[key]: 
                    st.add(item)

        ii += 1
    return ii + 1


path1 = 'inputPartial_20221223.txt'
path2 = 'inputFull_20221223.txt'

print(part1(path1))
print(part1(path2))
print(part2(path1))
print(part2(path2))


