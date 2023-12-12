# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:52:43 2023

@author: Leo Zhang
"""
from collections import Counter

path = 'inputPartial_20231207.txt'

def classify(cards): 
    cnter = Counter(cards)
    if len(cnter) == 1: 
        return 7
    if len(cnter) == 2: 
        if cnter[cards[0]] in [1, 4]: 
            return 6
        else: 
            return 5
    if len(cnter) == 3: 
        if max(cnter.values()) == 3: 
            return 4
        return 3
    if len(cnter) == 4: 
        return 2
    return 1

def rename(cards): 
    dic = {'T': ':', 'J': ';', 'Q': '<', 'K': '=', 'A': '>'}
    newcards = [dic.get(item, item) for item in cards]
    return ''.join(newcards)

def classify1(cards): 
    cnter = Counter(cards)
    if cnter['J'] == 0: 
        return classify(cards)
    else: 
        if len(cnter) in [1, 2]: 
            return 7
        if len(cnter) == 3: 
            if cnter['J'] in [2, 3]: 
                return 6
            if cnter['J'] == 1: 
                if max(cnter.values()) == 3: 
                    return 6
                else: 
                    return 5
        if len(cnter) == 4: 
            if cnter['J'] == 2: 
                return 4
            if cnter['J'] == 1: 
                return 4
        if len(cnter) == 5: 
            return 2
        
def rename1(cards): 
    dic = {'T': ':', 'J': '.', 'Q': '<', 'K': '=', 'A': '>'}
    newcards = [dic.get(item, item) for item in cards]
    return ''.join(newcards)

def calc1(path):
    ls = []
    with open(path, 'r') as f:
        for line in f:
            tmp_ls = line[:-1].split(' ')
            tmp_ls[1] = int(tmp_ls[1])
            ls.append(tmp_ls)
    
    ls_new = sorted(ls, key=lambda x:(classify(x[0]), rename(x[0])))
    res = 0
    for i in range(len(ls_new)): 
        res += (i + 1) * ls_new[i][1]
    return res

def calc2(path):
    ls = []
    with open(path, 'r') as f:
        for line in f:
            tmp_ls = line[:-1].split(' ')
            tmp_ls[1] = int(tmp_ls[1])
            ls.append(tmp_ls)
    
    ls_new = sorted(ls, key=lambda x:(classify1(x[0]), rename1(x[0])))
    res = 0
    for i in range(len(ls_new)): 
        res += (i + 1) * ls_new[i][1]
    return res

print(calc1(path))
print(calc2(path))
            
