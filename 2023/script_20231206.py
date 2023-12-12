# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:50:57 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231206.txt'

def func1(path): 
    i = 0
    with open(path, 'r') as f:
        for line in f:
            if i == 0: 
                ls_times = line[:-1].split(': ')[1].split(' ')
                ls_times = [int(item) for item in ls_times if item]
            if i == 1:
                ls_diss = line[:-1].split(': ')[1].split(' ')
                ls_diss = [int(item) for item in ls_diss if item]
            i += 1
    
    res = []
    for i in range(4): 
        time = ls_times[i]
        dis = ls_diss[i]
        tmp_res = 0
        for i in range(time + 1): 
            speed = i
            time_left = time - i
            if speed * time_left >= dis: 
                tmp_res += 1
        res.append(tmp_res)
    
    init = 1
    for item in res: 
        init *= item
    return init

print(func1(path))

def func2(path): 
    i = 0
    with open(path, 'r') as f:
        for line in f:
            if i == 0: 
                ls_times = line[:-1].split(': ')[1].split(' ')
                ls_times = [item for item in ls_times if item]
            if i == 1:
                ls_diss = line[:-1].split(': ')[1].split(' ')
                ls_diss = [item for item in ls_diss if item]
            i += 1
    
    time = int(''.join(ls_times))
    dis = int(''.join(ls_diss))
    
    # equation is x * (time - x) = dis
    # if we get the two roots we know how many solutions that qualified for 
    # x * (time - x) >= dis
    # x ^ 2 - time * x + dis = 0
    # two root = time / 2 +- sqrt(time ^ 2 - 4 * dis)
    root1 = (time - (time ** 2 - 4 * dis) ** 0.5) / 2
    root2 = (time + (time ** 2 - 4 * dis) ** 0.5) / 2
    if root1 != int(root1): 
        root1 = int(root1) + 1
    if root2 != int(root2): 
        root2 = int(root2)
    return root2 - root1 + 1
print(func2(path))
