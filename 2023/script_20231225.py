# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:33:28 2023

@author: Leo Zhang
"""
path = 'inputPartial_20231225.txt'
from collections import defaultdict
# import networkx as nx
# dic = defaultdict(list)
# ls_tps = []
# dic_val_idx = {}
# dic_idx_val = {}
# idx = 0

# G = nx.Graph()  # Replace with your actual graph

# with open(path, 'r') as f:
#     for line in f:
#         key, values = line[:-1].split(': ')
#         ls_values = values.split(' ')
#         if not key in dic_val_idx: 
#             dic_val_idx[key] = idx
#             dic_idx_val[idx] = key
#             idx += 1
#         for val in ls_values: 
#             if not val in dic_val_idx: 
#                 dic_val_idx[val] = idx
#                 dic_idx_val[idx] = val
#                 idx += 1
#             dic[dic_val_idx[key]].append(dic_val_idx[val])
#             dic[dic_val_idx[val]].append(dic_val_idx[key])
#             G.add_edges_from([(dic_val_idx[val], dic_val_idx[key])])
#             ls_tps.append(tuple(sorted([dic_val_idx[key], dic_val_idx[val]])))

# print(dic)
# print(G)
# for i in range(n_tps - 2): 
#     for j in range(i + 1, n_tps - 1): 
#         for k in range(j + 1, n_tps): 
#             if j % 1000 == 0: 
#                 print('j', j)
#             flag = 0 
#             for x, y in [ls_tps[i], ls_tps[j], ls_tps[k]]: 
#                 queue = [x]
#                 seen = set([x])
#                 while queue: 
#                     node = queue.pop(0)
#                     for newnd in dic[node]: 
#                         if newnd not in seen and tuple(sorted([node, newnd])) != ls_tps[i] and tuple(sorted([node, newnd])) != ls_tps[j] and tuple(sorted([node, newnd])) != ls_tps[k]: 
#                             if newnd == y: 
#                                 flag = 1
#                                 break
#                             seen.add(newnd)
#                             queue.append(newnd)
#                 if flag == 1: 
#                     break
#                 else: 
#                     res.append([i, j, k])
#                     break
    
# print([ls_tps[item] for item in res[0]])

        
import networkx as nx

path = 'inputPartial_20231225.txt'
dic = defaultdict(list)
ls_tps = []
dic_val_idx = {}
dic_idx_val = {}
idx = 0

G = nx.Graph()  # Replace with your actual graph
with open(path, 'r') as f:
    for line in f:
        key, values = line[:-1].split(': ')
        ls_values = values.split(' ')
        if not key in dic_val_idx: 
            dic_val_idx[key] = idx
            dic_idx_val[idx] = key
            idx += 1
        for val in ls_values: 
            if not val in dic_val_idx: 
                dic_val_idx[val] = idx
                dic_idx_val[idx] = val
                idx += 1
            dic[dic_val_idx[key]].append(dic_val_idx[val])
            dic[dic_val_idx[val]].append(dic_val_idx[key])
            
            G.add_edge(dic_val_idx[val], dic_val_idx[key], capacity=1)
            # print(dic_val_idx[val], dic_val_idx[key])
            ls_tps.append(tuple(sorted([dic_val_idx[key], dic_val_idx[val]])))

# print(max(dic_idx_val.keys()))
            
st_tps = set(ls_tps)
start = 0
end = max(dic_idx_val.keys())
cut_value, partition = nx.minimum_cut(G, start, end)
reachable, non_reachable = partition
cutset = set()
for u, nbrs in ((n, G[n]) for n in reachable):
    cutset.update((u, v) for v in nbrs if v in non_reachable)
print(sorted(cutset))
cutset = [tuple(sorted(item)) for item in cutset]
# cut_value == sum(G.edges[u, v]["capacity"] for (u, v) in cutset)
# from networkx.algorithms.flow import shortest_augmenting_path
# cut_value == nx.minimum_cut(G, "x", "y", flow_func=shortest_augmenting_path)[0]


seen = set()
res = []
for key in range(max(dic_idx_val.keys()) + 1): 
    # print(key)
    if key in seen: 
        continue
    else: 
        cnt = 1
        queue = [key]
        seen.add(key)
        while queue: 
            # print(key, queue)
            key0 = queue.pop(0)
            for newkey in dic[key0]: 
                if newkey not in seen and tuple(sorted([key0, newkey])) not in cutset: 
                    queue.append(newkey)
                    seen.add(newkey)
                    cnt += 1
        res.append(cnt)
print(res)





