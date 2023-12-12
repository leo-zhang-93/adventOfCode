# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:30 2022

@author: Leo Zhang
"""

# https://adventofcode.com/2022/day/14
path = 'inputPartial_20221214.txt'
res = 0

ls_coords = []
l = float('inf')
r = -float('inf')
u = float('inf')
d = -float('inf')

with open(path, 'r') as f: 
    for line in f:
        ls_tmp = line[:-1].split(' -> ')
        coords = []
        for item in ls_tmp:
            y, x = item.split(',')
            y = int(y)
            x = int(x)
            coords.append([x, y])
            l = min(l, y)
            r = max(r, y)
            u = min(u, x)
            d = max(d, x)
        ls_coords.append(coords)



# print(ls_coords)
## part 1
# left_offset = l
# m = d + 1
# n = r - l + 1
# # print(m, n, l, d)
# mat = [['.'] * n for _ in range(m)]
# for ls in ls_coords: 
#     for i in range(len(ls)): 
#         x, y = ls[i]
#         y -= l
#         if i == 0: 
#             mat[x][y] = '#'
#             prev = [x, y]
#         else: 
#             prevx, prevy = prev
#             if x == prevx: 
#                 for jj in range(min(y, prevy), max(y, prevy) + 1): 
#                     mat[x][jj] = '#'
#             else: 
#                 for ii in range(min(x, prevx), max(x, prevx) + 1): 
#                     mat[ii][y] = '#'
#             prev = [x, y]

# start_y = 500 - l
# def drop(): 
#     for i in range(m): 
#         if i == m - 1: 
#             return True
#         if i == 0: 
#             y = start_y
#         if y == 0 or y == n - 1: 
#             return True
#         if mat[i + 1][y] != '.': 
#             if mat[i + 1][y - 1] == '.': 
#                 y -= 1
#             elif mat[i + 1][y + 1] == '.': 
#                 y += 1
#             else: 
#                 mat[i][y] = '#'
#                 return False

# cnt = 0
# while True: 
#     cnt += 1
#     if drop(): 
#         break

# for ls in mat: 
#     print(''.join(ls))
# print(cnt)

## part2

m = d + 1
n = r + 2 * m
# print(m, n, l, d)
mat = [['.'] * n for _ in range(m)]
for ls in ls_coords: 
    for i in range(len(ls)): 
        x, y = ls[i]
        y
        if i == 0: 
            mat[x][y] = '#'
            prev = [x, y]
        else: 
            prevx, prevy = prev
            if x == prevx: 
                for jj in range(min(y, prevy), max(y, prevy) + 1): 
                    mat[x][jj] = '#'
            else: 
                for ii in range(min(x, prevx), max(x, prevx) + 1): 
                    mat[ii][y] = '#'
            prev = [x, y]

mat += [['.'] * n]
mat += [['#'] * n]
m += 2

# for ls in mat: 
#     print(''.join(ls))

cnt = 0
start_y = 500

def drop(): 
    for i in range(m): 
        if i == m - 1: 
            return True
        if i == 0: 
            y = start_y
        if y == 0 or y == n - 1: 
            return True
        if mat[i + 1][y] != '.': 
            if mat[i + 1][y - 1] == '.': 
                y -= 1
            elif mat[i + 1][y + 1] == '.': 
                y += 1
            else: 
                mat[i][y] = '#'
                return False
            
while True: 
    drop()
    cnt += 1
    if mat[0][start_y] == '#': 
        break
# drop()
    
print(cnt)
# for ls in mat: 
#     print(''.join(ls))


            
        