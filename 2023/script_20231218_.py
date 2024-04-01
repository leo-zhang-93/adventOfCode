# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:27:50 2023

@author: Leo Zhang
"""
from collections import defaultdict
import numpy as np
path = 'inputPartial_20231218.txt'
moves = []
        
with open(path, 'r') as f:
    for line in f:
        a, b, c = line[:-1].split(' ')
        c = c[1:-1]
        dirct = 'RDLU'[int(c[-1])]
        l = int(c[1:-1], 16)
        moves.append([dirct, l])
# with open(path, 'r') as f:
#     for line in f:
#         a, b, c = line[:-1].split(' ')
#         moves.append([a, int(b)])
# item = moves.pop(0)
# moves.append(item)
moves = moves[13:] + moves[:13]
print(moves)

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

# print(len(moves))
cnts_inner = [0] * len(moves)

for i in range(len(moves)): 
    d, l = moves[i]
    if prev_d is None: 
        init_deg = dic_deg[d]
        prev_d = d
    else: 
        change = 0
        if prev_d == 'L': 
            change = -dic_deg[d]
        elif prev_d == 'R': 
            change = dic_deg[d]
        elif prev_d == 'U': 
            change = dic_deg[d] - 90
        else: 
            change = -(dic_deg[d] - 90)
        init_deg += change
        if change == 90:
            # print(i, prev_d, d)
            cnts_inner[i - 1] += 1
            cnts_inner[i] += 1
        prev_d = d

print(init_deg)
print(cnts_inner)

res = 0
for i in range(len(moves)):
    ## this is related to the starting corner. 
    ## this is specific to outer corner and facing southwest
    ## otherwise we need to adjust the things below
    d, l = moves[i]
    prex, prey = ls[-1]
    if d == 'U': 
        if prey < 0:
            change = -np.float64(prey) * np.float64(l + 1 - cnts_inner[i]) / 2
        else: 
            change = -np.float64(prey) * np.float64((l + 1 - cnts_inner[i])) / 2
    elif d == 'D': 
        if prey > 0: 
            change = np.float64(prey + np.sign(prey)) * np.float64(l + 1 - cnts_inner[i]) / 2
        else: 
            change = np.float64(prey - np.sign(prey)) * np.float64(l + 1 - cnts_inner[i]) / 2
    elif d == 'R': 
        if prex > 0: 
            change = np.float64(prex + np.sign(prex)) * np.float64(l + 1 - cnts_inner[i]) / 2
        else: 
            change = np.float64(prex - np.sign(prex)) * np.float64(l + 1 - cnts_inner[i]) / 2
    else: # L
        if prex < 0: 
            change = -np.float64(prex) * np.float64(l + 1 - cnts_inner[i]) / 2
        else: 
            change = -np.float64(prex) * np.float64(l + 1 - cnts_inner[i]) / 2
    dx, dy = dic_dirs[d]
    dx *= l
    dy *= l
    ls.append([prex + dx, prey + dy])
    res += change
    # print(i, change, d, prex, prey, l, cnts_inner[i])
    # print(res)
    # print()

print(res)
    
    