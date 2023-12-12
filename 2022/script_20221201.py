# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 23:30:03 2022

@author: Leo Zhang
"""
path = 'inputFull_20221201.txt'

res = [0]
num1 = 0
num2 = 0
num3 = 0

with open(path, 'r') as f:
    for line in f: 
        if line == '\n':
            val = res[-1]
            if val > num1: 
                num2, num3 = num1, num2
                num1 = val
            elif num2 < val <= num1: 
                num3 = num2
                num2 = val
            elif num3 < val <= num2: 
                num3 = val
            
            res.append(0)
        else: 
            val = int(line[:-1])
            res[-1] += val

val = res[-1]
if val > num1: 
    num1 = val
    num2, num3 = num1, num2
elif num2 < val <= num1: 
    num2 = val
    num3 = num2
elif num3 < val <= num2: 
    num3 = val
print(sum([num3, num2, num1]))

            