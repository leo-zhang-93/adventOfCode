# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 00:03:25 2022

@author: Leo Zhang
"""

def part1(path):
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            ls.append(line[:-1])
    n = len(ls)
    cnt = (n - 1) * 4
    seen = set()
    for i in range(1, n - 1): 
        queue = [ls[i][0]]
        for j in range(1, n - 1):
            if not queue: 
                queue.append(ls[i][j])
            elif ls[i][j] > queue[-1]: 
                    queue.append(ls[i][j])
            else: 
                continue
            if (i, j) not in seen: 
                cnt += 1
                seen.add((i, j))
                
    for i in range(1, n - 1): 
        queue = [ls[i][-1]]
        for j in range(n - 2, 0, -1):
            if not queue: 
                queue.append(ls[i][j])
            elif ls[i][j] > queue[-1]: 
                    queue.append(ls[i][j])
            else: 
                continue
            if (i, j) not in seen: 
                cnt += 1
                seen.add((i, j))
    
    for j in range(1, n - 1): 
        queue = [ls[0][j]]
        for i in range(1, n - 1):
            if not queue: 
                queue.append(ls[i][j])
            elif ls[i][j] > queue[-1]: 
                    queue.append(ls[i][j])
            else: 
                continue
            if (i, j) not in seen: 
                cnt += 1
                seen.add((i, j))
    
    for j in range(1, n - 1): 
        queue = [ls[-1][j]]
        for i in range(n - 2, 0, -1):
            if not queue: 
                queue.append(ls[i][j])
            elif ls[i][j] > queue[-1]: 
                    queue.append(ls[i][j])
            else: 
                continue
            if (i, j) not in seen: 
                cnt += 1
                seen.add((i, j))
    
    return cnt

def part2(path):
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            ls.append(line[:-1])
    n = len(ls)
    mx = 0
    for i0 in range(1, n - 1): 
        for j0 in range(1, n - 1): 
            val = ls[i0][j0]
            p1, p2, p3, p4 = [1] * 4
            i, j = i0 - 1, j0
            while i > 0 and ls[i][j] < val: 
                i -= 1
                p1 += 1
            i, j = i0 + 1, j0
            while i < n - 1 and ls[i][j] < val: 
                i += 1
                p2 += 1
            i, j = i0, j0 - 1
            while j > 0 and ls[i][j] < val: 
                j -= 1
                p3 += 1
            i, j = i0, j0 + 1
            while j < n - 1 and ls[i][j] < val: 
                j += 1
                p4 += 1
            mx = max(mx, p1 * p2 * p3 * p4)
    return mx


path1 = 'inputPartial_20221208.txt'
path2 = 'inputFull_20221208.txt'

print(part1(path1))
print(part1(path2))
print(part2(path1))
print(part2(path2))            
                
        
        