# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:18:57 2022

@author: Leo Zhang
"""

# def part1(path, limit): 
#     directions = None
#     with open(path, 'r') as f:
#         for line in f:
#             directions = line[:-1]
#     seen = set()
#     ls_shapes = [1, 2, 3, 4, 5]
#     # - + J I O
#     maximum = [0]
#     def drop(shape, dir_idx): 
#         flag = 0
#         if shape == 1: 
#             bottom = [[maximum[0] + 4, 3], [maximum[0] + 4, 4], [maximum[0] + 4, 5], [maximum[0] + 4, 6]]
#             left = [[maximum[0] + 4, 3]]
#             right = [[maximum[0] + 4, 6]] 
#             res = []
#         elif shape == 2: 
#             bottom = [[maximum[0] + 5, 3], [maximum[0] + 4, 4], [maximum[0] + 5, 5]]
#             left = [[maximum[0] + 6, 4], [maximum[0] + 5, 3], [maximum[0] + 4, 4]]
#             right = [[maximum[0] + 6, 4], [maximum[0] + 5, 5], [maximum[0] + 4, 4]]
#             res = [[maximum[0] + 5, 4]]
#         elif shape == 3: 
#             bottom = [[maximum[0] + 4, 3], [maximum[0] + 4, 4], [maximum[0] + 4, 5]]
#             left = [[maximum[0] + 6, 5], [maximum[0] + 5, 5], [maximum[0] + 4, 3]]
#             right = [[maximum[0] + 6, 5], [maximum[0] + 5, 5], [maximum[0] + 4, 5]] 
#             res = []
#         elif shape == 4: 
#             bottom = [[maximum[0] + 4, 3]]
#             left = [[maximum[0] + 7, 3], [maximum[0] + 6, 3], [maximum[0] + 5, 3], [maximum[0] + 4, 3]]
#             right = [[maximum[0] + 7, 3], [maximum[0] + 6, 3], [maximum[0] + 5, 3], [maximum[0] + 4, 3]]
#             res = []
#         else: 
#             bottom = [[maximum[0] + 4, 3], [maximum[0] + 4, 4]]
#             left = [[maximum[0] + 5, 3], [maximum[0] + 4, 3]]
#             right = [[maximum[0] + 5, 4], [maximum[0] + 4, 4]] 
#             res = []
            
#         while flag == 0: 
#             if directions[dir_idx] == '>': 
#                 tmp_flag = 0
#                 for x, y in right: 
#                     if y + 1 > 7 or (x, y + 1) in seen: 
#                         tmp_flag = 1
#                         break
#                 if tmp_flag == 0: 
#                     for ls in [bottom, left, right, res]: 
#                         for item in ls: 
#                             item[1] += 1
#             else: 
#                 tmp_flag = 0
#                 for x, y in left: 
#                     if y - 1 < 1 or (x, y - 1) in seen: 
#                         tmp_flag = 1
#                         break
#                 if tmp_flag == 0: 
#                     for ls in [bottom, left, right, res]: 
#                         for item in ls: 
#                             item[1] -= 1
#             dir_idx += 1
#             if dir_idx == len(directions): 
#                 dir_idx = 0
                
#             for x, y in bottom: 
#                 if x - 1 < 1 or (x - 1, y) in seen: 
#                     flag = 1
#                     break
#             if flag == 1: 
#                 tmp_max = -float('inf')
#                 for ls in [bottom, left, right, res]: 
#                     for item in ls: 
#                         seen.add((item[0], item[1]))
#                         tmp_max = max(tmp_max, item[0])
#                 maximum[0] = max(maximum[0], tmp_max)
#                 # print(shape, maximum[0], bottom)
#                 return dir_idx
#             else: 
#                 for ls in [bottom, left, right, res]: 
#                     for item in ls: 
#                         item[0] -= 1
        
#     cnt = 0
#     dir_idx = 0
#     while True: 
#         for shape in ls_shapes:
#             dir_idx = drop(shape, dir_idx)
#             cnt += 1
#             if cnt == limit: 
#                 return maximum[0]
#                 break
                
# path2 = 'inputFull_20221217.txt'
# path1 = 'inputPartial_20221217.txt'
# limit= 2022

# print(part1(path1, limit))
# print(part1(path2, limit))

path = 'inputFull_20221217.txt'
limit= 10091
directions = None
with open(path, 'r') as f:
    for line in f:
        directions = line[:-1]
seen = set()
ls_shapes = [1, 2, 3, 4, 5]
# - + J I O
maximum = [0]
count = [0]
def drop(shape, dir_idx): 
    flag = 0
    if shape == 1: 
        bottom = [[maximum[0] + 4, 3], [maximum[0] + 4, 4], [maximum[0] + 4, 5], [maximum[0] + 4, 6]]
        left = [[maximum[0] + 4, 3]]
        right = [[maximum[0] + 4, 6]] 
        res = []
    elif shape == 2: 
        bottom = [[maximum[0] + 5, 3], [maximum[0] + 4, 4], [maximum[0] + 5, 5]]
        left = [[maximum[0] + 6, 4], [maximum[0] + 5, 3], [maximum[0] + 4, 4]]
        right = [[maximum[0] + 6, 4], [maximum[0] + 5, 5], [maximum[0] + 4, 4]]
        res = [[maximum[0] + 5, 4]]
    elif shape == 3: 
        bottom = [[maximum[0] + 4, 3], [maximum[0] + 4, 4], [maximum[0] + 4, 5]]
        left = [[maximum[0] + 6, 5], [maximum[0] + 5, 5], [maximum[0] + 4, 3]]
        right = [[maximum[0] + 6, 5], [maximum[0] + 5, 5], [maximum[0] + 4, 5]] 
        res = []
    elif shape == 4: 
        bottom = [[maximum[0] + 4, 3]]
        left = [[maximum[0] + 7, 3], [maximum[0] + 6, 3], [maximum[0] + 5, 3], [maximum[0] + 4, 3]]
        right = [[maximum[0] + 7, 3], [maximum[0] + 6, 3], [maximum[0] + 5, 3], [maximum[0] + 4, 3]]
        res = []
    else: 
        bottom = [[maximum[0] + 4, 3], [maximum[0] + 4, 4]]
        left = [[maximum[0] + 5, 3], [maximum[0] + 4, 3]]
        right = [[maximum[0] + 5, 4], [maximum[0] + 4, 4]] 
        res = []
        
    while flag == 0: 
        if directions[dir_idx] == '>': 
            tmp_flag = 0
            for x, y in right: 
                if y + 1 > 7 or (x, y + 1) in seen: 
                    tmp_flag = 1
                    break
            if tmp_flag == 0: 
                for ls in [bottom, left, right, res]: 
                    for item in ls: 
                        item[1] += 1
        else: 
            tmp_flag = 0
            for x, y in left: 
                if y - 1 < 1 or (x, y - 1) in seen: 
                    tmp_flag = 1
                    break
            if tmp_flag == 0: 
                for ls in [bottom, left, right, res]: 
                    for item in ls: 
                        item[1] -= 1
        dir_idx += 1
        count[0] += 1
        if dir_idx == len(directions): 
            dir_idx = 0
            
        for x, y in bottom: 
            if x - 1 < 1 or (x - 1, y) in seen: 
                flag = 1
                break
        if flag == 1: 
            tmp_max = -float('inf')
            for ls in [bottom, left, right, res]: 
                for item in ls: 
                    seen.add((item[0], item[1]))
                    tmp_max = max(tmp_max, item[0])
            maximum[0] = max(maximum[0], tmp_max)
            # print(shape, maximum[0], bottom)
            return dir_idx
        else: 
            for ls in [bottom, left, right, res]: 
                for item in ls: 
                    item[0] -= 1
    
cnt = 0
dir_idx = 0
res = []
dic = {}
# while True: 
#     for shape in ls_shapes:
#         newdir_idx = drop(shape, dir_idx)
#         if shape == 1: 
#             tmp = []
#             for i in range(1, 8): 
#                 if (maximum[0], i) in seen: 
#                     tmp.append(i)
#             if (shape, dir_idx) not in dic: 
#                 dic[(shape, dir_idx)] = []
#             else: 
#                 dic[(shape, dir_idx)].append([cnt, tmp])
#             # print(dic[(shape, dir_idx)])
#         dir_idx = newdir_idx
#         cnt += 1
#     if cnt % limit == 0: 
#         print(cnt)
#     if cnt == limit * 10: 
#         break
            
while True: 
    for shape in ls_shapes:
        dir_idx = drop(shape, dir_idx)
        cnt += 1
        if cnt in [1600, 1600 + 1725, 1600 + 1725 * 2]: 
            print(maximum[0])
            break
    if cnt == 6000: 
        break
#         if cnt == 1: 
#             print(seen)
    

        
        
        
        