# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:21:55 2023

@author: Leo Zhang
"""
from collections import defaultdict

path = 'inputPartial_20231220.txt'
times = 1000
dic = {}
dic_typs = {'%': 'f', '&': 'c'}
dic_inputs = defaultdict(list)
with open(path, 'r') as f:
    for line in f:
        if line[0] == 'b': 
            key, ls = line[:-1].split(' -> ')
            ls = ls.split(', ')
            dic[key] = ['b', ls]
        else: 
            key, ls = line[:-1].split(' -> ')
            typ = key[0]
            key = key[1:]
            ls = ls.split(', ')
            dic[key] = [dic_typs[typ], ls]
        for item in ls: 
            dic_inputs[item].append(key)
# print(dic)
# print(dic['broadcaster'])
# print(dic_inputs)

dic_status = {}
ls_fkeys = []
ls_otherkeys = []
for key in dic.keys(): 
    if dic[key][0] == 'f': 
        ls_fkeys.append(key)
        dic_status[key] = ['off', 'low']
    else: 
        ls_otherkeys.append(key)
        dic_status[key] = ['on', 'low']
        
# print(dic_status)



# print(cnt)
# print(flag)
# if flag == 0: 
#     period = len(ls_cumuresult_low)
#     a, b = times // period, times % period
#     cnt_lows = a * ls_cumuresult_low[-1] + (b > 0) * ls_cumuresult_low[b - 1]
#     cnt_highs = a * ls_cumuresult_high[-1] + (b > 0) * ls_cumuresult_high[b - 1]
#     print(cnt_lows, cnt_highs)
#     print(cnt_lows * cnt_highs)
# else: 
#     print (ls_cumuresult_high[-1] * ls_cumuresult_low[-1])

## part 2
result_low = 0
result_high = 0

cnt = 0

ls_starts = ['cn', 'xk', 'rj', 'gf']
ls_chains = [[] for _ in range(4)]
for i in range(4): 
    start_key = ls_starts[i]
    seen = set([start_key])
    queue = [start_key]
    ls_chains[i].append(start_key)
    while queue: 
        node = queue.pop(0)
        if node not in dic: 
            continue
        for newnode in dic[node][1]: 
            if dic[newnode][0] == 'f': 
                queue.append(newnode)
                ls_chains[i].append(newnode)
## dr <-> cn
## sv <-> xk
## qz <-> rj
## sk <-> gf

ls_ckeys = ['dr', 'sv', 'qz', 'sk']
ls_results = []
for i in range(4): 
    on_keys = dic_inputs[ls_ckeys[i]]
    tmp_res = 0
    for j in range(len(ls_chains[i])): 
        fkey = ls_chains[i][j]
        if fkey in on_keys: 
            tmp_res += 2 ** (j)
    ls_results.append(tmp_res)

cnt = 1
ls_res_period = [[] for _ in range(4)]
dic_pos_second = {'mr': 0, 'rz': 1, 'kv': 2, 'jg': 3}
flag_period = 0
while True: 
    queue = [['low', 'broadcaster']]
    while queue: 
        this_pulse, node = queue.pop(0)
        if node in ['mr', 'rz', 'kv', 'jg']:
            if this_pulse =='low': 
                ls_res_period[dic_pos_second[node]].append(cnt)
            if min([len(item) for item in ls_res_period]) == 3:                 
                flag_period = 1
                break
        if node not in dic: 
            continue
        nd_type, nd_nexts = dic[node]
        new_pulse_type = 'low'
        if nd_type == 'b': 
            new_pulse_type = 'low'
            dic_status[node][1] = new_pulse_type
            for next_node in nd_nexts: 
                queue.append([new_pulse_type, next_node])
        elif nd_type == 'f': 
            if this_pulse == 'low': 
                if dic_status[node][0] == 'on': 
                    new_pulse_type = 'low'
                    dic_status[node][0] = 'off'
                else: 
                    new_pulse_type = 'high'
                    dic_status[node][0] = 'on'
                dic_status[node][1] = new_pulse_type
                for next_node in nd_nexts: 
                    queue.append([new_pulse_type, next_node])   
        else: 
            flag = 0
            for input_node in dic_inputs[node]: 
                if dic_status[input_node][1] == 'low': 
                    new_pulse_type = 'high'
                    flag = 1
                    break
            if flag == 0: 
                new_pulse_type = 'low'
            dic_status[node][1] = new_pulse_type
            for next_node in nd_nexts: 
                queue.append([new_pulse_type, next_node]) 
    
    cnt += 1
    if flag_period == 1:
        break
    if cnt == 50000:
        break
print(ls_res_period)
print(cnt)
ls_period_starts = [item[0] for item in ls_res_period]
ls_period_length = [item[1] - item[0] for item in ls_res_period]

def mcf(x, y): 
    if y < x: 
        return mcf(y, x)
    if y % x == 0: 
        return x
    else: 
        return mcf(x, y % x)

init_val = ls_period_length[0]
print(ls_period_length)
for i in range(1, 4): 
    init_val = mcf(init_val, ls_period_length[i])
    print(init_val)

prod = 1
for item in ls_period_length: 
    prod *= item
print(prod)

  

            
