# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 04:30:54 2022

@author: Leo Zhang
"""

def part1(path): 
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            ls.append([*map(int, line[:-1].split(','))])
    
    from collections import defaultdict
    dic1 = defaultdict(list)
    dic2 = defaultdict(list)
    dic3 = defaultdict(list)
    
    for x, y, z in ls: 
        dic1[x, y].append(z)
        dic2[x, z].append(y)
        dic3[y, z].append(x)
    
    res = 0
    for dic in [dic1, dic2, dic3]: 
        for key in dic:
            
            tmp_ls = sorted(dic[key])
            cluster = 0
            prev = None
            for item in tmp_ls: 
                if prev is None: 
                    prev = item
                elif item - prev > 1: 
                    cluster += 1
                    prev = item
                else: 
                    prev = item
            cluster += 1
            res += cluster * 2
    return res

def part2(path): 
    ls = []
    cubes = set()
    with open(path, 'r') as f:
        for line in f: 
            tmp = [*map(int, line[:-1].split(','))]
            ls.append(tmp)
            cubes.add(tuple(tmp))
    max_x = -float('inf')
    max_y = -float('inf')
    max_z = -float('inf')
    min_x = float('inf')
    min_y = float('inf')
    min_z = float('inf')
    for x, y, z in ls: 
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)

    
    queue = [[0, 0, 0]]
    seen = set((0, 0, 0))
    directions = [
        [0, 0, -1], 
        [0, 0, 1], 
        [0, -1, 0], 
        [0, 1, 0], 
        [-1, 0, 0], 
        [1, 0, 0],
        ]
    count_faces = 0
    seen_cubes = set()
    while queue: 
        x, y, z = queue.pop(0)
        # print('!', x, y, z)
        for dx, dy, dz in directions: 
            newx, newy, newz = x + dx, y + dy, z + dz
            # print('!!', newx, newy, newz)
            if min_x - 1 <= newx <= max_x + 1 and min_y - 1 <= newy <= max_y + 1 and min_z - 1 <= newz <= max_z + 1: 
                if (newx, newy, newz) in cubes: 
                    seen_cubes.add((newx, newy, newz))
                    count_faces += 1
                elif (newx, newy, newz) not in seen: 
                    queue.append([newx, newy, newz])
                    seen.add((newx, newy, newz))
    # print(len(seen), len(cubes), len(seen_cubes), (max_x + 2) * (max_y + 2) * (max_z + 2))
    return count_faces
    
                    
    

path1 = 'inputPartial_20221218.txt'
path2 = 'inputFull_20221218.txt'

# print(part1(path1))
# print(part1(path2))

print(part2(path1))
print(part2(path2))