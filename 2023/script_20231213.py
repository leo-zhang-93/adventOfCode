# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:53:41 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231213.txt'

ls = []
tmp_ls = []
with open(path, 'r') as f:
    for line in f:
        if line != '\n': 
            tmp_ls.append(line[:-1])
        else: 
            ls.append(tmp_ls)
            tmp_ls = []
    ls.append(tmp_ls)
# print(ls)

def checkv(ls, i): 
    u = i
    d = i + 1
    m = len(ls)
    flag = 1
    while u >= 0 and d < m: 
        if ls[u] != ls[d]: 
            flag = 0
            break
        u -= 1
        d += 1
    return flag

def slc(ls, j):    
    return ''.join([item[j] for item in ls])

def checkh(ls, j): 
    l = j
    r = j + 1
    n = len(ls[0])
    flag = 1
    while l >= 0 and r < n: 
        if slc(ls, l) != slc(ls, r): 
            flag = 0
            break
        l -= 1
        r += 1
    return flag       
    
nls = len(ls)
res = 0
factor = 100
ls_res = []
for i in range(nls): 
    tmp_ls = ls[i]
    m, n = len(tmp_ls), len(tmp_ls[0])
    flag = 0
    for t in range(0, m - 1): 
        if checkv(tmp_ls, t): 
            res += factor * (t + 1)
            ls_res.append(['v', t])
            flag = 1
            break
    if flag == 0: 
        for s in range(0, n - 1): 
            if checkh(tmp_ls, s): 
                res += s + 1
                ls_res.append(['h', s])
                break
print(res)

res = 0
for i in range(nls): 
    tmp_ls = ls[i]
    tmp_ls = [list(item) for item in tmp_ls]
    m, n = len(tmp_ls), len(tmp_ls[0])
    for ii in range(m): 
        for jj in range(n): 
            flag = 0
            if tmp_ls[ii][jj] == '.': 
                tmp_ls[ii][jj] = '#'
            else:  
                tmp_ls[ii][jj] = '.'
            for t in range(0, m - 1): 
                if checkv(tmp_ls, t) and (ls_res[i][0] != 'v' or ls_res[i][1] != t): 
                    res += factor * (t + 1)
                    flag = 1
                    break
            if flag == 0: 
                for s in range(0, n - 1): 
                    if checkh(tmp_ls, s) and (ls_res[i][0] != 'h' or ls_res[i][1] != s): 
                        res += s + 1
                        flag = 1
                        break
            if tmp_ls[ii][jj] == '.': 
                tmp_ls[ii][jj] = '#'
            else:  
                tmp_ls[ii][jj] = '.'
            if flag == 1: 
                break
        if flag == 1: 
            break
print(res)
        
            
    
    
            