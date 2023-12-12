# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:41:15 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231212.txt'

def readFile(path): 
    ls_lines = []
    with open(path, 'r') as f:
        for line in f:
            tmp_line = line[:-1]
            pattern, nums = tmp_line.split(' ')
            ls_nums = list(map(int, nums.split(',')))
            ls_lines.append([pattern.strip('.'), ls_nums])
    return ls_lines

dic = {}
def calc(string, ls, start, withsep): 
    if (string, tuple(ls), start, withsep) in dic: 
        return dic[(string, tuple(ls), start, withsep)]
    if not ls: 
        if '#' in string: 
            dic[(string, tuple(ls), start, withsep)] = 0
            return 0
        else: 
            dic[(string, tuple(ls), start, withsep)] = 1
            return 1
    if len(string) < sum(ls) + len(ls) - 1: 
        dic[(string, tuple(ls), start, withsep)] = 0
        return 0
    if string[0] == '#': 
        if start and not withsep: 
            dic[(string, tuple(ls), start, withsep)] = 0
            return 0
        newls = ls.copy()
        if newls[0] == 1: 
            res = calc(string[1:], newls[1:], True, False)
            dic[(string, tuple(ls), start, withsep)] = res
            return res
        else: 
            newls[0] -= 1
            res = calc(string[1:], newls, False, False)
            dic[(string, tuple(ls), start, withsep)] = res
            return res
    elif string[0] == '?': 
        if start and not withsep: 
            res = calc(string[1:], ls, True, True)
            dic[(string, tuple(ls), start, withsep)] = res
            return res
        if start: 
            res = 0
            newls = ls.copy()
            res += calc(string[1:], newls, True, True)
            if newls[0] == 1:
                res += calc(string[1:], newls[1:], True, False)
            else: 
                newls[0] -= 1
                res += calc(string[1:], newls, False, False)
            dic[(string, tuple(ls), start, withsep)] = res
            return res
        else: 
            newls = ls.copy()
            if newls[0] == 1:
                res = calc(string[1:], newls[1:], True, False)
                dic[(string, tuple(ls), start, withsep)]= res
                return res
            else: 
                newls[0] -= 1
                res = calc(string[1:], newls, False, False)
                dic[(string, tuple(ls), start, withsep)] = res
                return res
            
    else: ## string[0] == '.'
        if not start: 
            dic[(string, tuple(ls), start, withsep)] = 0
            return 0
        else: 
            res = calc(string[1:], ls, start, True)
            dic[(string, tuple(ls), start, withsep)] = res
            return res

def calc1(path):   
    ls_lines = readFile(path)
    result = 0
    for st, ls in ls_lines: 
        result += calc(st, ls, True, True)
    return result

def calc2(path, times): 
    ls_lines = readFile(path)
    result = 0      
    for st, ls in ls_lines: 
        result += calc('?'.join([st] * times), ls * times, True, True)
    return result

times = 5
print(calc1(path))
print(calc2(path, times))    



    
    