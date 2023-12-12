# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:15:25 2022

@author: Leo Zhang
"""

## partial test
from collections import deque
import numpy as np

# ls_ls = [
#       [79, 98], 
#       [54, 65, 75, 74], 
#       [79, 60, 97], 
#       [74], 
#       ]
# print(sum([len(item) for item in ls_ls]))

# ls_funcs = [
#     lambda x: x * 19, 
#     lambda x: x + 6, 
#     lambda x: x ** 2, 
#     lambda x: x + 3,        
#     ]

# ls_divisors = [
#     23, 
#     19, 
#     13, 
#     17,
#     ]


# ls_tests = [
#     [2, 3], 
#     [2, 0], 
#     [1, 3], 
#     [0, 1],     
#     ]

ls_ls = [
      [52, 78, 79, 63, 51, 94], 
      [77, 94, 70, 83, 53], 
      [98, 50, 76], 
      [92, 91, 61, 75, 99, 63, 84, 69], 
      [51, 53, 83, 52], 
      [76, 76], 
      [75, 59, 93, 69, 76, 96, 65], 
      [89], 
      ]

ls_funcs = [
    lambda x: x * 13, 
    lambda x: x + 3, 
    lambda x: x ** 2, 
    lambda x: x + 5, 
    lambda x: x + 7,      
    lambda x: x + 4,   
    lambda x: x * 19, 
    lambda x: x + 2,   
    ]

ls_divisors = [
    5, 
    7, 
    13, 
    11,
    3, 
    2, 
    17, 
    19,
    ]

ls_tests = [
    [1, 6], 
    [5, 3], 
    [0, 6], 
    [5, 7],     
    [2, 0], 
    [4, 7], 
    [1, 3], 
    [2, 4],
    ]

ls_ls = [deque(item) for item in ls_ls]

divisor = 1
for item in ls_divisors: 
    divisor *= item

cnts = [0] * len(ls_ls)

for rnd in range(10000): 
    for i in range(len(ls_ls)): 
        while ls_ls[i]: 
            worry = ls_ls[i].popleft()
            new_worry = ls_funcs[i](worry)
            if new_worry % ls_divisors[i] == 0: 
                new_idx = ls_tests[i][0]
            else: 
                new_idx = ls_tests[i][1]
            ls_ls[new_idx].append(new_worry % divisor)
            cnts[i] += 1
print(cnts)
cnts = sorted(cnts)
print(cnts[-1] * cnts[-2])
            