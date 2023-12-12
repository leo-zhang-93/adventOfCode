# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:20:08 2022

@author: Leo Zhang
"""

def calc(path, y0): 
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            s1, s2 = line[:-1].split(': ')
            s11, s12 = s1.split(' ')[-2:]
            s21, s22 = s2.split(' ')[-2:]
            val11 = int(s11[2:-1])
            val12 = int(s12[2:])
            val21 = int(s21[2:-1])
            val22 = int(s22[2:])
            ls.append([val11, val12, val21, val22])
    
    ls_ranges = []
    
    for x1, y1, x2, y2 in ls: 
        distance = abs(x1 - x2) + abs(y1 - y2)
        if distance >= abs(y1 - y0): 
            r = x1 + (distance - abs(y0 - y1))
            l = x1 - (distance - abs(y0 - y1))
            ls_ranges.append([l, r])
    
    ls_ranges = sorted(ls_ranges, key=lambda x: [x[0], -x[1]])
    # print(ls_ranges)
    ls_res = []
    left, right = 0, 0
    for x, y in (ls_ranges + [[float('inf'), float('inf')]]): 
        if not left: 
            left = x
            right = y
        else: 
            if x > right: 
                ls_res.append([left, right])
                left, right = x, y
            elif y > right: 
                right = y
    
    print(ls_res)
    st = set()
    for x1, y1, x2, y2 in ls: 
        if y2 == y0 and x2 >= ls_res[0][0] and x2 <= ls_res[0][1]: 
            st.add((x2, y2))
    print(st)
    return ls_res[0][1] - ls_res[0][0] + 1 - len(st)

## part 1
# print(calc('inputPartial_20221215.txt', 10))
# print(calc('inputFull_20221215.txt', 2000000))

## part 2

def calc_(path, y0): 
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            s1, s2 = line[:-1].split(': ')
            s11, s12 = s1.split(' ')[-2:]
            s21, s22 = s2.split(' ')[-2:]
            val11 = int(s11[2:-1])
            val12 = int(s12[2:])
            val21 = int(s21[2:-1])
            val22 = int(s22[2:])
            ls.append([val11, val12, val21, val22])
    
    ls_ranges = []
    
    for x1, y1, x2, y2 in ls: 
        distance = abs(x1 - x2) + abs(y1 - y2)
        if distance >= abs(y1 - y0): 
            r = x1 + (distance - abs(y0 - y1))
            l = x1 - (distance - abs(y0 - y1))
            ls_ranges.append([l, r])
    
    ls_ranges = sorted(ls_ranges, key=lambda x: [x[0], -x[1]])
    # print(ls_ranges)
    ls_res = []
    left, right = 0, 0
    for x, y in (ls_ranges + [[float('inf'), float('inf')]]): 
        if not left: 
            left = x
            right = y
        else: 
            if x > right + 1: 
                ls_res.append([left, right])
                left, right = x, y
            elif y > right: 
                right = y
    
    return ls_res
    # st = set()
    # for x1, y1, x2, y2 in ls: 
    #     if y2 == y0 and x2 >= ls_res[0][0] and x2 <= ls_res[0][1]: 
    #         st.add((x2, y2))
    # print(st)
    # return ls_res[0][1] - ls_res[0][0] + 1 - len(st)

path = 'inputPartial_20221215.txt'
max_y = 20
for i in range(max_y): 
    res = calc_(path, i)
    if i % 100000 == 0: 
        print(i)
    if len(res) > 1 or res[0][0] > 0 or res[0][1] < max_y: 
        print(i, res)
        