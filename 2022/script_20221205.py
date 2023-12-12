# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:46:46 2022

@author: Leo Zhang
"""

def func1(path):
    flag = 0
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            if i == 0: 
                n = len(line)
                cnt = n // 4
                ls = [[] for _ in range(cnt)] 
            if line[0] == '[' or line.strip(' ')[0] == '[':
                for j in range(cnt): 
                    val = line[4 * j + 1]
                    if val != ' ': 
                        ls[j].append(line[4 * j + 1])
            elif line[0] == 'm': 
                if flag == 0: 
                    for ii in range(cnt): 
                        ls[ii] = ls[ii][::-1]
                    flag = 1                    
                tmp_ls = line[:-1].split(' ')
                ct, sidx, eidx = int(tmp_ls[1]), int(tmp_ls[3]), int(tmp_ls[5])
                for ii in range(ct): 
                    ls[eidx - 1].append(ls[sidx - 1].pop())
    return ''.join([item[-1] for item in ls])

def func2(path):
    flag = 0
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            if i == 0: 
                n = len(line)
                cnt = n // 4
                ls = [[] for _ in range(cnt)] 
            if line[0] == '[' or line.strip(' ')[0] == '[':
                for j in range(cnt): 
                    val = line[4 * j + 1]
                    if val != ' ': 
                        ls[j].append(line[4 * j + 1])
            elif line[0] == 'm': 
                if flag == 0: 
                    for ii in range(cnt): 
                        ls[ii] = ls[ii][::-1]
                    flag = 1                    
                tmp_ls = line[:-1].split(' ')
                ct, sidx, eidx = int(tmp_ls[1]), int(tmp_ls[3]), int(tmp_ls[5])
                ls[eidx - 1] += ls[sidx - 1][-ct:]
                ls[sidx - 1] = ls[sidx - 1][:-ct]
    return ''.join([item[-1] for item in ls])
    
path1 = "inputPartial_20221205.txt"   
path2 = "inputFull_20221205.txt"
    
print(func1(path1))
print(func1(path2))  
print(func2(path1))
print(func2(path2)) 