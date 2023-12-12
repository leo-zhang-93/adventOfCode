# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:01:45 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231203.txt'

def tomatrix(path): 
    ls = []
    with open(path, 'r') as f:
        for line in f:
            ls.append(line[:-1] + '.')
    return ls


def part1(path): 
    mat = tomatrix(path)
    m, n = len(mat), len(mat[0])
    
    def check(val): 
        return ord(val) != 46 and (ord(val) < 48 or ord(val) > 57)
    
    res = 0
    for i in range(m): 
        l = None
        tmp_val = ''
        for j in range(n):
            val = mat[i][j]
            if 48 <= ord(val) <= 57: 
                if l is None: 
                    l = j
                tmp_val += val
            else: 
                if l is None: 
                    continue
                flag = 0
                if i - 1 >= 0: 
                    for val_ in mat[i - 1][max(0, l - 1):min(n, j + 1)]: 
                        if check(val_): 
                            res += int(tmp_val)
                            flag = 1
                if flag == 0 and i + 1 <= m - 1: 
                    for val_ in mat[i + 1][max(0, l - 1):min(n, j + 1)]: 
                        if check(val_): 
                            res += int(tmp_val)
                            flag = 1
                if flag == 0 and l - 1 >= 0: 
                    if check(mat[i][l - 1]): 
                        res += int(tmp_val)
                        flag = 1
                if flag == 0:
                    if check(mat[i][j]): 
                        res += int(tmp_val)
                        flag = 1
                # if flag == 1: 
                #     print(i, j, tmp_val)
                l = None
                tmp_val = ''
        return res
print(part1(path))


def part2(path): 
    mat = tomatrix(path)
    m, n = len(mat), len(mat[0])
    
    def check_two(x, y): 
        directions = [
                [-1, -1], 
                [-1, 0], 
                [-1, 1], 
                [0, -1],
                [0, 1], 
                [1, -1], 
                [1, 0], 
                [1, 1]
                ]
        cnt = 0
        pos = []
        for dx, dy in directions: 
            newx, newy = x + dx, y + dy
            if 0 <= newx < m and 0 <= newy < n: 
                val = mat[newx][newy]
                if 48 <= ord(val) <= 57: 
                    cnt += 1
                    pos.append([newx, newy])
        if cnt <= 1: 
            return 0
        else: 
            dic = {}
            for x0, y0 in pos: 
                val0 = mat[x0][y0]
                newy0 = y0 - 1
                while newy0 >= 0 and 48 <= ord(mat[x0][newy0]) <= 57: 
                    val0 = mat[x0][newy0] + val0
                    newy0 -= 1
                
                newy1 = y0 + 1
                while newy1 < n and 48 <= ord(mat[x0][newy1]) <= 57: 
                    val0 = val0 + mat[x0][newy1]
                    newy1 += 1
                dic[(x0, newy0)] = int(val0)
            
            if len(dic) == 2: 
                ls_res = list(dic.values())
                # print(x, y, ls_res)
                return ls_res[0] * ls_res[1]
            return 0
            
    
    res = 0
    for i in range(m): 
        for j in range(n): 
            val = mat[i][j]
            if val == '*': 
                res += check_two(i, j)
    return res
print(part2(path))
            
            
            

            
                    
            
                