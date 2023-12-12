# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:57:36 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231209.txt'
res = []
with open(path, 'r') as f:
    for line in f:
        tmp_ls = list(map(int, line[:-1].split(' ')))
        res.append(tmp_ls)
    
from collections import Counter

def calc(ls): 
    ls_diff = []
    n = len(ls)
    for i in range(1, n): 
        ls_diff.append(ls[i] - ls[i - 1])
    cnter = Counter(ls_diff)
    if cnter[0] == len(ls_diff): 
        return ls[-1]
    else: 
        addition = calc(ls_diff)
        return ls[-1] + addition

result = 0 
for ls in res: 
    result += calc(ls)
print(result)

result = 0 
for ls in res: 
    result += calc(ls[::-1])
print(result)
        