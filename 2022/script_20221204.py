# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:26:08 2022

@author: Leo Zhang
"""

def func1(path): 
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            part1, part2 = line[:-1].split(',')
            l1, r1 = map(int, part1.split('-'))
            l2, r2 = map(int, part2.split('-'))
            if (l1 <= l2 and r1 >= r2) or (l1 >= l2 and r1 <= r2):
                res += 1
    return res

def func2(path): 
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            part1, part2 = line[:-1].split(',')
            l1, r1 = map(int, part1.split('-'))
            l2, r2 = map(int, part2.split('-'))
            if r1 < l2 or r2 < l1: 
                continue
            res += 1
    return res

path1 = 'inputPartial_20221204.txt'
path2 = 'inputFull_20221204.txt'

print(func1(path1))
print(func1(path2))
print(func2(path1))
print(func2(path2))