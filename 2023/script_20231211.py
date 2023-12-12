# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:39:31 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231211.txt'

def readFile(path): 
    res = []
    with open(path, 'r') as f:
        for line in f:
            tmp = line[:-1]
            res.append(list(tmp))
    return res

def calc(path, factor): 
    res = readFile(path)
    m, n = len(res), len(res[0])
    set1 = set(range(1, m + 1))
    set2 = set(range(1, n + 1))

    ls = []
    for i in range(m): 
        for j in range(n): 
            val = res[i][j]
            if val == '#':
                ls.append([i, j])
                set1.discard(i)
                set2.discard(j)

    lsi = sorted(set1)
    lsj = sorted(set2)

    dic = {}
    def bs(val, idx): 
        if (val, idx) in dic: 
            return dic[(val, idx)]
        if idx == 0: 
            ls = lsi
        else: 
            ls = lsj
        def bs_(l, r): 
            if val < ls[l]:
                return l
            if val > ls[r]: 
                return r + 1
            if r - l == 1: 
                return r
            mid = (l + r) // 2
            if val < ls[mid]: 
                tmp = bs_(l, mid)
                return tmp
            else: 
                tmp = bs_(mid, r)
                return tmp
            
        tmp = bs_(0, len(ls) - 1)
        dic[(val, idx)] = tmp
        return tmp

    nls = len(ls)
    result = 0
    for ii in range(nls - 1): 
        for jj in range(ii + 1, nls): 
            x1, y1 = ls[ii]
            x2, y2 = ls[jj]
            
            x_add = abs(bs(x2, 0) - bs(x1, 0))
            y_add = abs(bs(y2, 1) - bs(y1, 1))
            tmp = abs(x1 - x2) + abs(y1 - y2) + (factor - 1) * (x_add + y_add)
            result += tmp
    return result

factor1 = 2
factor2 = 1000000
print(calc(path, factor1))
print(calc(path, factor2))
