# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:54:00 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231205.txt'
with open(path, 'r') as f:
    i = 0
    ls_seeds = []
    lsls = [[] for _ in range(7)]
    flag = 0
    for line in f:
        if i == 0: 
            ls_seeds = list(map(int, line[:-1].split(' ')[1:]))
        elif line == '\n': 
            continue
        elif line.startswith('seed'): 
            flag = 1
        elif line.startswith('soil'): 
            flag = 2
        elif line.startswith('fertilizer'): 
            flag = 3
        elif line.startswith('water'): 
            flag = 4
        elif line.startswith('light'): 
            flag = 5
        elif line.startswith('temperature'): 
            flag = 6
        elif line.startswith('humidity'): 
            flag = 7
        else: 
            lsls[flag - 1].append(list(map(int, line[:-1].split(' '))))
        i += 1

for i in range(7): 
    lsls[i] = sorted(lsls[i], key=lambda x: x[1])

def check(val, ls): 
    n = len(ls)
    if val < ls[0][1]: 
        return val
    if val > ls[n - 1][1] + ls[n - 1][2] - 1: 
        return val
    else: 
        for i in range(n): 
            if ls[i][1] <= val <= ls[i][1] + ls[i][2] - 1: 
                return val - ls[i][1] + ls[i][0]
            elif ls[i][1] + ls[i][2] - 1 < val < ls[i + 1][1]: 
                return val

min_res = float('inf')
# for seed in ls_seeds:
#     val = seed
#     for i in range(7):
#         val = check(val, lsls[i])
#     # print(val)
#     min_res = min(min_res, val)
# print('!', min_res)

## there are 7 transform but all are segmented linear. 
## also the results function we still have slope = 1 per each segment. 
## if we know the start of each segment (from the beginning) and sort it 
## we just need to check the final results of these start points. 

def calc(x): 
    val = x
    for i in range(7):
        val = check(val, lsls[i])
    return val

def check1(val, ls): 
    n = len(ls)
    if val <= ls[0][0]: 
        return val
    if val >= ls[n - 1][0] + ls[n - 1][2] - 1: 
        return val
    else: 
        for i in range(n): 
            if ls[i][0] <= val <= ls[i][0] + ls[i][2] - 1: 
                return val - ls[i][0] + ls[i][1]
            elif ls[i][0] + ls[i][2] - 1 < val < ls[i + 1][0]: 
                return val


ls = []
for j in range(6, 0, -1): 
    ls += [item[1] for item in lsls[j]]
    tmp_ls = []
    for item in ls: 
        tmp_ls.append(check1(item, sorted(lsls[j - 1])))
    ls = tmp_ls
tmp_ls += [item[1] for item in lsls[0]]
tmp_ls = sorted(set(tmp_ls))

ls_seeds1 = [[ls_seeds[2 * i], ls_seeds[2 * i] + ls_seeds[2 * i + 1] - 1] for i in range(10)]
ls_seeds1 = sorted(ls_seeds1)

res = float('inf')
idx = 0
for x, y in ls_seeds1: 
    while idx < len(tmp_ls) and tmp_ls[idx] < x: 
        idx += 1
    tmp_res = calc(x)
    print(x, y, x, tmp_res)
    res = min(res, tmp_res)
    while idx < len(tmp_ls) and tmp_ls[idx] < y: 
        tmp_res = calc(tmp_ls[idx])
        print(x, y, tmp_ls[idx], tmp_res)
        res = min(res, calc(tmp_ls[idx]))
        idx += 1
    tmp_res = calc(y)
    print(x, y, y, tmp_res)
    res = min(res, tmp_res)
    
    
print(res)
    
        
    
    





        