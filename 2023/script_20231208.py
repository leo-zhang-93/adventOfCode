# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:56:06 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231208.txt'
#path = 'inputPartial_20231208_.txt'

def calc1(path): 
    i = 0
    dic = {}
    with open(path, 'r') as f:
        for line in f:
            if i == 0: 
                ls_directions = line[:-1]
            elif i == 1:
                pass
            else: 
                key, vals = line[:-1].split(' = ')
                ls_vals = vals[1:-1].split(', ')
                dic[key] = ls_vals
            i += 1

    ndirections = len(ls_directions)
    i = 0
    init = 'AAA'
    while True:
        dirct = ls_directions[i % ndirections]
        if dirct == 'L': 
            init = dic[init][0]
        else: 
            init = dic[init][1]
        if init == 'ZZZ': 
            break
        i += 1
    return i + 1

def calc2(path): 
    i = 0
    ls_as = set()
    ls_zs = set()
    dic = {}
    ls_as = set()
    ls_zs = set()
    with open(path, 'r') as f:
        for line in f:
            if i == 0: 
                ls_directions = line[:-1]
                # print(ls_directions)
            elif i == 1:
                pass
            else: 
                # print(line)
                key, vals = line[:-1].split(' = ')
                ls_vals = vals[1:-1].split(', ')
                dic[key] = ls_vals
                if key[-1] == 'A': 
                    ls_as.add(key)
                if ls_vals[0][-1] == 'A': 
                    ls_as.add(ls_vals[0])
                if ls_vals[1][-1] == 'A': 
                    ls_as.add(ls_vals[1])
                if key[-1] == 'Z': 
                    ls_zs.add(key)
                if ls_vals[0][-1] == 'Z': 
                    ls_zs.add(ls_vals[0])
                if ls_vals[1][-1] == 'Z': 
                    ls_zs.add(ls_vals[1])
            i += 1
    
    ndirections = len(ls_directions)
    inits = list(ls_as)
    res = [[] for _ in range(len(inits))]
    for j in range(len(inits)): 
        val = inits[j]
        i = 0
        while True: 
            dirct = ls_directions[i % ndirections]
            if dirct == 'L': 
                val = dic[val][0]
            else: 
                val = dic[val][1]
            if val in ls_zs: 
                res[j].append([val, i + 1])
            i += 1
            if i == 100000: 
                break
    ls_periods = []
    for ls in res: 
        base = ls[0][1]
        period = ls[1][1] - ls[0][1]
        ls_periods.append([period, base])

    def mcf(x, y): 
        if y < x: 
            return mcf(y, x)
        if y % x == 0:
            return x
        else: 
            return mcf(x, y % x)
    
    ls_periods_ = [item[1] for item in ls_periods]
    val = ls_periods_[0]
    for i in range(1, len(ls_periods_)): 
        val = mcf(val, ls_periods_[i])
    mcf_val = val
    
    result = 1
    for val in ls_periods_: 
        result *= val // mcf_val
    return result * mcf_val
    
print(calc1(path))
print(calc2(path))
