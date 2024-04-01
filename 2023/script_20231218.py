# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:45:26 2023

@author: Leo Zhang
"""
from collections import defaultdict
path = 'inputPartial_20231218.txt'
moves = []
with open(path, 'r') as f:
    for line in f:
        a, b, c = line[:-1].split(' ')
        moves.append([a, int(b)])
        
# with open(path, 'r') as f:
#     for line in f:
#         a, b, c = line[:-1].split(' ')
#         c = c[1:-1]
#         dirct = 'RDLU'[int(c[-1])]
#         l = int(c[1:-1], 16)
#         moves.append([dirct, l])
# print(moves)

initx = 0
inity = 0
ls = [[initx, inity]]
dic_dirs = {
    'U': [1, 0], 
    'D': [-1, 0],
    'L': [0, -1], 
    'R': [0, 1], 
    }

dic_deg = {
    'U': 90,
    'D': -90, 
    'L': 180, 
    'R': 0
    }

dic_rights = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}

lmost = 0
rmost = 0
dmost = 0
umost = 0

prev_d = None
init_deg = 0

border = set([(0, 0)])
dic_inner = defaultdict(list)
for d, l in moves: 
    if prev_d is None: 
        init_deg = dic_deg[d]
        prev_d = d
    else: 
        if prev_d == 'L': 
            init_deg -= dic_deg[d]
        elif prev_d == 'R': 
            init_deg += dic_deg[d]
        elif prev_d == 'U': 
            init_deg += dic_deg[d] - 90
        else: 
            init_deg -= dic_deg[d] - 90
        prev_d = d
    prex, prey = ls[-1]
    dx, dy = dic_dirs[d]
    for length in range(0, l + 1):
        border.add((prex + length * dx, prey + length * dy))
        dic_inner[(prex + length * dx, prey + length * dy)].append(dic_rights[d])
    dx *= l
    dy *= l
    ls.append([prex + dx, prey + dy])
    lmost = min(lmost, prey + dy)
    rmost = max(rmost, prey + dy)
    dmost = min(dmost, prex + dx)
    umost = max(umost, prex + dx)

# print(init_deg)
# print(umost, dmost, lmost, rmost)
# print(ls)
# print(len(border))
# newm = umost - dmost + 1
# newn = rmost - lmost + 1
# newgrid = [['o'] * newn for _ in range(newm)]
# for i in range(newm): 
#     for j in range(newn): 
#         if (i + dmost, j + lmost) in border: 
#             newgrid[newm - 1 - i][j] = '*'

# def write_list(fname, ls):
#     with open(fname, "w") as fhandle:
#       for item in ls:
#         fhandle.write('{}\n'.format(''.join(item)))

# write_list('filename.txt', newgrid)

seen = set()
result = 0
for i in range(dmost, umost + 1): 
    for j in range(lmost, rmost + 1): 
        if (i, j) in seen or (i, j) in border: 
            continue
        x, y = i, j
        queue = [[x, y]]
        tmp_cnt = 0
        flag = None
        while queue: 
            x0, y0 = queue.pop(0)
            for dx, dy in dic_dirs.values(): 
                if dmost <= x0 + dx <= umost and lmost <= y0 + dy <= rmost: 
                    if flag is None and (x0 + dx, y0 + dy) in border: 
                        for newd in dic_inner[(x0 + dx, y0 + dy)]:
                            innerx, innery = dic_dirs[newd]
                            if innerx + dx == 0 and innery + dy == 0: 
                                flag = 1
                        if flag is None: 
                            flag = 0
                    elif (x0 + dx, y0 + dy) not in border and (x0 + dx, y0 + dy) not in seen: 
                        queue.append([x0 + dx, y0 + dy])
                        seen.add((x0 + dx, y0 + dy))
                        tmp_cnt += 1
        print(i, j, flag, tmp_cnt)
        if flag == 1: 
            result += tmp_cnt

# print(border)
# print(result)
# print(len(border))

print(result + len(border))
                        


