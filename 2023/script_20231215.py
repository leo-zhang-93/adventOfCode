# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:55:46 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231215.txt'

def readInput(path): 
    txt = ''
    with open(path, 'r') as f:
        for line in f:
            txt = line[:-1]
    ls = txt.split(',')
    return ls

def hashhash(string): 
    res = 0
    for char in string: 
        val = ord(char)
        res += val
        res *= 17
        res %= 256
    return res

def calc1(path): 
    ls = readInput(path)
    result = 0
    for item in ls: 
        result += hashhash(item)
    return result

def calc2(path): 
    ls = readInput(path)
    placeholders = [[] for _ in range(256)]
    ls_set = [set() for _ in range(256)]
    
    for item in ls: 
        if '=' in item: 
            label, focal = item.split('=')
            focal = int(focal)
            hashlabel = hashhash(label)
            if label not in ls_set[hashlabel]: 
                ls_set[hashlabel].add(label)
                placeholders[hashlabel].append([label, focal])
            else: 
                for itm in placeholders[hashlabel]: 
                    if itm[0] == label: 
                        itm[1] = focal
                        break
        else: 
            label = item[:-1]
            hashlabel = hashhash(label)
            if label not in ls_set[hashlabel]: 
                continue
            else: 
                ls_set[hashlabel].discard(label)
                for i in range(len(placeholders[hashlabel])): 
                    if placeholders[hashlabel][i][0] == label: 
                        break
                placeholders[hashlabel].pop(i)
    
    result = 0
    for i in range(256): 
        if not len(placeholders[i]): 
            continue
        else: 
            tmp_res = 0
            for j in range(len(placeholders[i])): 
                tmp_res += (1 + j) * placeholders[i][j][1]
            result += (i + 1) * tmp_res
    return result

print(calc1(path))
print(calc2(path))
        