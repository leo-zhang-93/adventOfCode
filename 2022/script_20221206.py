# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 00:00:12 2022

@author: Leo Zhang
"""

def part1(path, length): 
    from collections import defaultdict
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            ls.append(line)
    string = ls[0][:-1]
    n = len(string)
    
    queue = []
    seen = defaultdict(int)
    for i in range(n): 
        val = string[i]
        if len(queue) < length:  
            queue.append(val)
            seen[val] += 1
        else: 
            tmp = queue.pop(0)
            seen[tmp] -= 1
            if seen[tmp] == 0: 
                seen.pop(tmp)
            queue.append(val)
            seen[val] += 1
        if len(seen) == length: 
            return i + 1

path1 = 'inputPartial_20221206.txt'
path2 = 'inputFull_20221206.txt'
print(part1(path1, 4))
print(part1(path2, 4))

print(part1(path1, 14))
print(part1(path2, 14))

        
