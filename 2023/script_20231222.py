# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 20:10:43 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231222.txt'
from collections import defaultdict
ls_bricks = []
minx = float('inf')
maxx = -float('inf')
miny = float('inf')
maxy = -float('inf')
ii = 0
with open(path, 'r') as f:
    for line in f:
        tmp_ls = list(map(int, line[:-1].replace('~', ',').split(',')))
        tmp_ls = [tmp_ls[:3], tmp_ls[3:]]
        tmp_ls = sorted(tmp_ls, key=lambda x: [x[2], x[0], x[1]])
        minx = min(minx, tmp_ls[0][0], tmp_ls[1][0])
        maxx = max(maxx, tmp_ls[0][0], tmp_ls[1][0])
        miny = min(miny, tmp_ls[0][1], tmp_ls[1][1])
        maxy = max(maxy, tmp_ls[0][1], tmp_ls[1][1])              
        ls_bricks.append(tmp_ls)
        
ls_bricks = sorted(ls_bricks, key=lambda x: [x[0][2], x[1][2]])
# print(ls_bricks)
print(minx, maxx, miny, maxy)
lookdown = [[[0, None] for _ in range(maxx + 1)] for _ in range(maxy + 1)]

st_cannotmove = set()
n = len(ls_bricks)
dic_links = defaultdict(list)
dic_nexts = defaultdict(list)
for i in range(n): 
    [x1, y1, z1], [x2, y2, z2] = ls_bricks[i]
    if x1 == x2 and y1 == y2: 
        lookdown[x1][y1][0] += (z2 - z1 + 1)
        if lookdown[x1][y1][1] is not None: 
            st_cannotmove.add(lookdown[x1][y1][1])
            dic_links[i].append(lookdown[x1][y1][1])
            dic_nexts[lookdown[x1][y1][1]].append(i)
        lookdown[x1][y1][1] = i
    elif x1 == x2: 
        tmp_dic = defaultdict(set)
        max_tmp_height = -float('inf')
        for yy in range(y1, y2 + 1): 
            tmp_height = lookdown[x1][yy][0]
            if lookdown[x1][yy][1] is not None: 
                tmp_dic[tmp_height].add(lookdown[x1][yy][1])
            max_tmp_height = max(tmp_height, max_tmp_height)
        dic_links[i] += list(tmp_dic[max_tmp_height])
        for item in tmp_dic[max_tmp_height]: 
            dic_nexts[item].append(i)
        if len(tmp_dic[max_tmp_height]) == 1: 
            prev_brick = list(tmp_dic[max_tmp_height])[0]
            st_cannotmove.add(prev_brick)
        for yy in range(y1, y2 + 1): 
            lookdown[x1][yy][0] = max_tmp_height + 1
            lookdown[x1][yy][1] = i
        # print(i, tmp_dic)
    elif y1 == y2: 
        tmp_dic = defaultdict(set)
        max_tmp_height = -float('inf')
        for xx in range(x1, x2 + 1): 
            tmp_height = lookdown[xx][y1][0]
            if lookdown[xx][y1][1] is not None: 
                tmp_dic[tmp_height].add(lookdown[xx][y1][1])
            max_tmp_height = max(tmp_height, max_tmp_height)
        dic_links[i] += list(tmp_dic[max_tmp_height])
        for item in tmp_dic[max_tmp_height]: 
            dic_nexts[item].append(i)
        if len(tmp_dic[max_tmp_height]) == 1: 
            prev_brick = list(tmp_dic[max_tmp_height])[0]
            st_cannotmove.add(prev_brick)
        for xx in range(x1, x2 + 1): 
            lookdown[xx][y1][0] = max_tmp_height + 1
            lookdown[xx][y1][1] = i
        # print(i, tmp_dic)
# print(lookdown)
            
# print(st_cannotmove)
print(len(ls_bricks), len(st_cannotmove))
# print(st_cannotmove)
print(len(ls_bricks) - len(st_cannotmove))
# print(dic_links)
# print()
# print(dic_nexts)

def calc(key): 
    queue = [key]
    seen = set([key])
    while queue: 
        node = queue.pop(0)
        for item in dic_nexts[node]: 
            if item not in seen: 
                if len(dic_links[item]) == 1: 
                    seen.add(item)
                    queue.append(item)
                else: 
                    flag = 0
                    for item_spt in dic_links[item]: 
                        if item_spt not in seen:
                            flag = 1
                            break
                    if flag == 0: 
                        seen.add(item)
                        queue.append(item)
    return len(seen) - 1

result = 0
for key in sorted(st_cannotmove): 
    tmp = calc(key)
    print(key, tmp)
    result += tmp
print(result)
                
                
                
    
    

    
            
            
            
        
        
        
    
