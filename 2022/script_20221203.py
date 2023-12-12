# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:08:36 2022

@author: Leo Zhang
"""

def func1(path):
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            tmp_line = line[:-1]
            tmp_n = len(tmp_line)
            s1 = tmp_line[:tmp_n // 2]
            s2 = tmp_line[tmp_n // 2:]
            char = set(s1).intersection(set(s2)).pop()
            if ord(char) >= 97: 
                res += ord(char) - 96
            else: 
                res += ord(char) - 38
    return res


def func2(path): 
    res = 0
    with open(path, 'r') as f: 
        cnt = 0
        for line in f: 
            tmp_line = line[:-1]
            if cnt == 0: 
                st1 = set(tmp_line)
                cnt += 1
            elif cnt == 1: 
                st2 = set(tmp_line)
                cnt += 1
            else: 
                st3 = set(tmp_line)
                char = st1.intersection(st2).intersection(st3).pop()
                if ord(char) >= 97: 
                    res += ord(char) - 96
                else: 
                    res += ord(char) - 38
                cnt = 0
    return res
            
path1 = 'inputPartial_20221203.txt'
path2 = 'inputFull_20221203.txt'
print(func1(path1))
print(func1(path2))

print(func2(path1))
print(func2(path2))            
            
            