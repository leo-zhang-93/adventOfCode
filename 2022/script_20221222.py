# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:32:25 2022

@author: Leo Zhang
"""

def part1(path):
    ls = []
    instructions = ''
    flag = 0
    with open(path, 'r') as f:
        for line in f: 
            if line == '\n': 
                flag = 1
            elif flag == 0: 
                ls.append(line[:-1])
            else: 
                instructions = line[:-1]
    m = len(ls)
    n = 0
    for line in ls: 
        n = max(len(line), n)
    for i in range(m): 
        ls[i] += ' ' * (n - len(ls[i]))
    
    for j in range(n): 
        if ls[0][j] == '.': 
            start = [0, j]
            break
    
    ls_instructions = []
    cumu = ''
    for char in instructions + '$': 
        if char not in 'RL$': 
            cumu += char
        else: 
            ls_instructions.append(int(cumu))
            if char in 'LR':
                ls_instructions.append(char)    
            cumu = ''
    # print(instructions + '$')
    # print(ls_instructions)
    
    dic_rows = {}
    dic_cols = {}
    
    for i in range(m): 
        flag = 0
        res = []
        for j in range(n):
            val = ls[i][j]
            if flag == 0:
                if val in '.#': 
                    flag = 1
                    res.append(j)
            elif flag == 1 and val == ' ':
                res.append(j - 1)
                dic_rows[i] = res
                break
        if i not in dic_rows: 
            res.append(n - 1)
            dic_rows[i] = res
            
    for j in range(n): 
        flag = 0
        res = []
        for i in range(m):
            val = ls[i][j]
            if flag == 0: 
                if val in '.#': 
                    flag = 1
                    res.append(i)
            elif flag == 1 and val == ' ': 
                res.append(i - 1)
                dic_cols[j] = res
                break 
        if j not in dic_cols: 
            res.append(m - 1)
            dic_cols[j] = res
    
    d = [0, 1]
    x, y = start
    
    for action in ls_instructions: 
        if isinstance(action, int): 
            for step in range(action): 
                newx = x + d[0]
                newy = y + d[1]
                if 0 <= newx < m and 0 <= newy < n: 
                    if ls[newx][newy] == '.': 
                        x, y = newx, newy
                    elif ls[newx][newy] == '#': 
                        break
                    else: 
                        if d[1] == 1: 
                            newy = dic_rows[newx][0]
                        elif d[1] == -1: 
                            newy = dic_rows[newx][1]
                        elif d[0] == 1: 
                            newx = dic_cols[newy][0]
                        elif d[0] == -1: 
                            newx = dic_cols[newy][1]
                        if ls[newx][newy] == '.': 
                            x, y = newx, newy
                        else:  # '#'
                            break    
                else: 
                    if newx == m: 
                        newx = dic_cols[newy][0]
                    elif newx == -1: 
                        newx = dic_cols[newy][1]
                    elif newy == n: 
                        newy = dic_rows[newx][0]
                    elif newy == -1: 
                        newy = dic_rows[newx][1]
                    if ls[newx][newy] == '.': 
                        x, y = newx, newy
                    else:  # '#'
                        break  
        elif action == 'R': 
            if d[1] == 1: 
                d = [1, 0]
            elif d[1] == -1: 
                d = [-1, 0]
            elif d[0] == 1: 
                d = [0, -1]
            elif d[0] == -1: 
                d = [0, 1]
        else: 
            if d[1] == 1: 
                d = [-1, 0]
            elif d[1] == -1: 
                d = [1, 0]
            elif d[0] == 1: 
                d = [0, 1]
            elif d[0] == -1: 
                d = [0, -1]

    print(x, y, d)
    res = 0
    res += (x + 1) * 1000 + (y + 1) * 4
    if d[1] == -1: 
        res += 2
    elif d[0] == 1: 
        res += 1
    elif d[0] == -1: 
        res += 3
    return res

def part2(path, length):
    ls = []
    instructions = ''
    flag = 0
    with open(path, 'r') as f:
        for line in f: 
            if line == '\n': 
                flag = 1
            elif flag == 0: 
                ls.append(line[:-1])
            else: 
                instructions = line[:-1]
    m = len(ls)
    n = 0
    for line in ls: 
        n = max(len(line), n)
    for i in range(m): 
        ls[i] += ' ' * (n - len(ls[i]))
    
    for j in range(n): 
        if ls[0][j] == '.': 
            start = [0, j]
            break
    
    ls_instructions = []
    cumu = ''
    for char in instructions + '$': 
        if char not in 'RL$': 
            cumu += char
        else: 
            ls_instructions.append(int(cumu))
            if char in 'LR':
                ls_instructions.append(char)    
            cumu = ''
    # print(instructions + '$')
    # print(ls_instructions)
    
    dic_rows = {}
    dic_cols = {}
    
    for i in range(m): 
        flag = 0
        res = []
        for j in range(n):
            val = ls[i][j]
            if flag == 0:
                if val in '.#': 
                    flag = 1
                    res.append(j)
            elif flag == 1 and val == ' ':
                res.append(j - 1)
                dic_rows[i] = res
                break
        if i not in dic_rows: 
            res.append(n - 1)
            dic_rows[i] = res
            
    for j in range(n): 
        flag = 0
        res = []
        for i in range(m):
            val = ls[i][j]
            if flag == 0: 
                if val in '.#': 
                    flag = 1
                    res.append(i)
            elif flag == 1 and val == ' ': 
                res.append(i - 1)
                dic_cols[j] = res
                break 
        if j not in dic_cols: 
            res.append(m - 1)
            dic_cols[j] = res
    
    d = [0, 1]
    x, y = start
    
    for action in ls_instructions: 
        if isinstance(action, int): 
            for step in range(action): 
                newx = x + d[0]
                newy = y + d[1]
                if 0 <= newx < m and 0 <= newy < n: 
                    if ls[newx][newy] == '.': 
                        x, y = newx, newy
                        continue
                    elif ls[newx][newy] == '#': 
                        break
                        # print('?', newx, newy, d)
                d0 = d
                if d[1] == 1: 
                    if 0 <= x <= (length - 1): 
                        newx = (length * 3 - 1) - newx
                        newy = dic_rows[newx][1]
                        d = [0, -1]
                    elif length <= x <= (length * 2 - 1):
                        newy = (length * 2 - 1) + newx - (length - 1)
                        newx = dic_cols[newy][1]
                        d = [-1, 0]
                    elif (length * 2) <= x <= (length * 3 - 1): 
                        newx = (length * 3 - 1) - newx
                        newy = dic_rows[newx][1]
                        d = [0, -1]
                    elif (length * 3) <= x <= (length * 4 - 1): 
                        newy = (length - 1) + newx - (length * 3 - 1)
                        newx = dic_cols[newy][1]
                        d = [-1, 0]
                elif d[1] == -1: 
                    if 0 <= x <= (length - 1): 
                        newx = (length * 3 - 1) - newx
                        newy = dic_rows[newx][0]
                        d = [0, 1]
                    elif length <= x <= (length * 2 - 1): 
                        newy = newx - length
                        newx = dic_cols[newy][0]
                        d = [1, 0]
                    elif (length * 2) <= x <= (length * 3 - 1): 
                        newx = (length * 3 - 1) - newx
                        newy = dic_rows[newx][0]
                        d = [0, 1]
                    elif (length * 3) <= x <= (length * 4 - 1): 
                        newy = newx - (length * 2)
                        newx = dic_cols[newy][0]
                        d = [1, 0]
                elif d[0] == 1: 
                    if 0 <= y <= (length - 1): 
                        newy += (length * 2)
                        newx = dic_cols[newy][0]
                    elif length <= y <= (length * 2 - 1): 
                        newx = (length * 3 - 1) + newy - (length - 1)
                        newy = dic_rows[newx][1]
                        d = [0, -1]
                    elif (length * 2) <= y <= (length * 3 - 1): 
                        newx = (length - 1) + newy - (length * 2 - 1)
                        newy = dic_rows[newx][1]
                        d = [0, -1]
                elif d[0] == -1: 
                    if 0 <= y <= (length - 1): 
                        newx = newy + length
                        newy = dic_rows[newx][0]
                        d = [0, 1]
                    elif length <= y <= (length * 2 - 1): 
                        newx = newy + (length * 2)
                        newy = dic_rows[newx][0]
                        d = [0, 1]
                    elif (length * 2) <= y <= (length * 3 - 1): 
                        newy -= (length * 2)
                        newx = dic_cols[newy][1]
                # print('!', newx, newy, d)
                if ls[newx][newy] == '.': 
                    x, y = newx, newy
                else:  # '#'
                    d = d0
                    break    

        elif action == 'R': 
            if d[1] == 1: 
                d = [1, 0]
            elif d[1] == -1: 
                d = [-1, 0]
            elif d[0] == 1: 
                d = [0, -1]
            elif d[0] == -1: 
                d = [0, 1]
        else: 
            if d[1] == 1: 
                d = [-1, 0]
            elif d[1] == -1: 
                d = [1, 0]
            elif d[0] == 1: 
                d = [0, 1]
            elif d[0] == -1: 
                d = [0, -1]
    #     print(action, x, y, d)
    # print(x, y, d)
    res = 0
    res += (x + 1) * 1000 + (y + 1) * 4
    if d[1] == -1: 
        res += 2
    elif d[0] == 1: 
        res += 1
    elif d[0] == -1: 
        res += 3
    return res

path1 = 'inputPartial_20221222.txt'
path3 = 'inputPartial_20221222_1.txt'
path2 = 'inputFull_20221222.txt'

# print(part1(path1))
# print(part1(path2))
print(part2(path2, 50))
print(part2(path3, 4))




