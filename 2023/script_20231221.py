# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:02:30 2023

@author: Leo Zhang
"""

from collections import defaultdict
path = 'inputPartial_20231221.txt'
grid = []
i = 0
i_s = 0
with open(path, 'r') as f:
    for line in f:
        grid.append(list(line[:-1]))
        if 'S' in line: 
            i_s = i
            j_s = line.index('S')
        i += 1

m, n = len(grid), len(grid[0])
print(m, n, i_s, j_s)

## all and the new ones from previous
dic = {0: [set([(i_s, j_s)]), set([(i_s, j_s)])]}
queue = [i_s, j_s]

directions = [
    [-1, 0], 
    [1, 0], 
    [0, -1], 
    [0, 1]
    ]

def call_value(x, y):
    return grid[x % m][y % n]

for i in range(1, 460):
    st_prev_all, st_prev_new = dic[i - 1]
    if i == 1: 
        st_prev2_all, st_prev2_new = set(), set()
    else: 
        st_prev2_all, st_prev2_new = dic[i - 2]
    st_new_all = set()
    st_new_new = set()
    for x, y in st_prev_new: 
        for dx, dy in directions: 
            if call_value(x + dx, y + dy) in '.S':
                if (x + dx, y + dy) in st_prev_all: 
                    st_new_all.add((x + dx, y + dy))
                elif (x + dx, y + dy) not in st_prev2_all:
                    st_new_new.add((x + dx, y + dy))
    st_new_all = st_prev2_all.union(st_new_all).union(st_new_new)
    dic[i] = [st_new_all.copy(), st_new_new.copy()]

for key in range(460):
    print(key, len(dic[key][0]), len(dic[key][1]))
    
"""
Notes. This second part is not an algo problem at all. 
If you do not look into the input, you could never figure it out. 
The input is like a diamond shape centered at the center. You will notice a band surrounding the diamond. 
And if you have a check, you will notice within that band, there is no cell as '#'. 
And for the 4 directions, if you start from 'S', there's also no '#' at all.
And them if you calculate the results for a broader range, e.g. up to 500 steps. 
You can find out some pattern, for 65 + 131k steps, 2 steps more, we have 4 * (65 + 131k + 2) more plots than 65 + 131k. 
This always holds, which means from 65 + 131k to 67 + 131k, the expansion hit no rock. 
If we see the number of steps in the question - 26501365, it's also a 65 + 131k (202300). 
We look into k = 1, 2, 3 and see the pattern is quadratic. 
We can calculate the parameters with the 3 values we get from our P1 solution and calcalate for k = 202300.
"""

# dic_res = defaultdict(int)
# for i in range(-10, m + 10): 
#     for j in range(-10, n + 10): 
#         val = abs(i - 65) + abs(j - 65)
#         if call_value(i, j) != '#': 
#             dic_res[val] += 1
# for key in range(0, 70): 
#     print(key, dic_res[key], key * 4 == dic_res[key])

        
# rounds = 100
# for i in range(1, rounds + 1):
#     st_prev_all, st_prev_new = dic[i - 1]
#     if i == 1: 
#         st_prev2_all, st_prev2_new = set(), set()
#     else: 
#         st_prev2_all, st_prev2_new = dic[i - 2]
#     st_new_all = set()
#     st_new_new = set()
#     for x, y in st_prev_new: 
#         for dx, dy in directions: 
#             if call_value(x + dx, y + dy) in '.S':
#                 if (x + dx, y + dy) in st_prev_all: 
#                     st_new_all.add((x + dx, y + dy))
#                 elif (x + dx, y + dy) not in st_prev2_all:
#                     st_new_new.add((x + dx, y + dy))
#     st_new_all = st_prev2_all.union(st_new_all).union(st_new_new)
#     dic[i] = [st_new_all.copy(), st_new_new.copy()]
#     if i % 100 == 0: 
#         print(i)

# for key in range(1, rounds + 1):
#     # if key in [6, 10, 50, 100, 500, 1000, 5000]:
#     #print(key, len(dic[key][0]), len(dic[key][1]))
#     tmp_cnt = 0
#     for i in range(m): 
#         for j in range(4 * n, 5 * n): 
#             if (i, j) in dic[key][0]: 
#                 tmp_cnt += 1
#     print(key, tmp_cnt)
    


        
                
    
    
