# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:51:53 2022

@author: Leo Zhang
"""

def part1(path):
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            if line[0] == 'n': 
                ls.append(['noop', 0])
            else: 
                action, x = line[:-1].split(' ')
                x = int(x)
                ls.append([action, x])
    
    res = []
    xx = 1
    cycle = 1
    
    for action, x in ls: 
        if action == 'addx': 
            res.append(xx)
            # print(cycle, xx, action, x)
            xx += x
            cycle += 1
            res.append(xx)
            # print(cycle, xx, action, x)
            cycle += 1
        else: 
            res.append(xx)
            # print(cycle, xx, action, x)
            cycle += 1
    ls_idx = range(19, len(res), 40)
    return sum([res[idx - 1] * (idx + 1) for idx in ls_idx])

path1 = 'inputPartial_20221210.txt'
path2 = 'inputFull_20221210.txt'

# print(part1(path1))
# print(part1(path2))


def part2(path): 
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            if line[0] == 'n': 
                ls.append(['noop', 0])
            else: 
                action, x = line[:-1].split(' ')
                x = int(x)
                ls.append([action, x])
    
    res = []
    xx = 1
    cycle = 1
    for action, x in ls: 
        if action == 'addx':
            for _ in range(2):
                if cycle % 40 == 1: 
                    res.append([])
                if xx - 1 <= cycle % 40 - 1 <= xx + 1: 
                    res[-1].append('#')
                else: 
                    res[-1].append('.')
                cycle += 1
            xx += x
        else: 
            if cycle % 40 == 1: 
                res.append([])
            if xx - 1 <= cycle % 40 - 1 <= xx + 1: 
                res[-1].append('#')
            else: 
                res[-1].append('.')
            cycle += 1
    for line in res: 
        print(''.join(line))
    
part2(path1)
part2(path2)