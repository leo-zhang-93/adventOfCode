# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:38:18 2022

@author: Leo Zhang
"""
path = 'inputPartial_20221202.txt'
ls = []
with open(path, 'r') as f:
    for line in f: 
        ls.append(line[:-1].split(' '))

## part1
# dic = {
#        'AA': 1 + 3, 
#        'AB': 2 + 6, 
#        'AC': 3 + 0, 
#        'BA': 1 + 0, 
#        'BB': 2 + 3, 
#        'BC': 3 + 6, 
#        'CA': 1 + 6, 
#        'CB': 2 + 0, 
#        'CC': 3 + 3,
#        }

# def calc(first, second):
#     return dic[first+second]

# ls_cases = [
#       'ABC', 
#       # 'ACB', 
#       # 'BAC', 
#       # 'BCA', 
#       # 'CAB', 
#       # 'CBA', 
#       ]

# max_res = 0
# for case in ls_cases: 
#     dic_tmp = {'XYZ'[i]: case[i] for i in range(3)}
#     res = 0
#     for game in ls: 
#         res += calc(game[0], dic_tmp[game[1]])
#     print(res, dic_tmp)
#     max_res = max(max_res, res)
# print(max_res)

## part 2
dic = {
       'AX': 0 + 3, 
       'AY': 3 + 1,
       'AZ': 6 + 2, 
       'BX': 0 + 1,
       'BY': 3 + 2, 
       'BZ': 6 + 3, 
       'CX': 0 + 2,
       'CY': 3 + 3,
       'CZ': 6 + 1,
       }    
res = 0
for case in ls: 
    res += dic[''.join(case)]
print(res)
    