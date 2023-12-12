# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:49:09 2022

@author: Leo Zhang
"""
import datetime

def part1(path, target_mnt): 
    from collections import defaultdict
    
    dic_rates = {}
    dic_paths = defaultdict(list)
    with open(path, 'r') as f:
        for line in f: 
            ls_tmp = line[:-1].replace("=", " ").replace(";","").replace(",","").split(' ')
            # print(ls_tmp[1], ls_tmp[5], ls_tmp[10:])
            dic_rates[ls_tmp[1]] = int(ls_tmp[5])
            dic_paths[ls_tmp[1]] += ls_tmp[10:]

    new_dic = {}
    
    summation = [0]
    def calc(mnt, curr, status): 
        tp = tuple(sorted(status))
        if (mnt, curr, tp) in new_dic: 
            return new_dic[(mnt, curr, tp)]
        if len(status) == len(dic_rates): 
            val = summation[0]
            new_dic[(mnt, curr, tp)] = (target_mnt - mnt) * val
            return (target_mnt - mnt) * val
        else: 
            if mnt == target_mnt: 
                val = summation[0]
                new_dic[(mnt, curr, tp)] = val
                return val
            else: 
                val = summation[0]
                res = 0
                for node in dic_paths[curr]: 
                    res = max(res, calc(mnt + 1, node, status.union({})))
                if curr not in status: 
                    if dic_rates[curr] > 0:
                        summation[0] += dic_rates[curr]
                        res = max(res, calc(mnt + 1, curr, status.union({curr})))
                        summation[0] -= dic_rates[curr]
                new_dic[(mnt, curr, tp)] = val + res
                return val + res
    print(datetime.datetime.now())
    val = calc(0, 'AA', set({'AA'}))
    print(val)
    print(datetime.datetime.now())
    return val


def part2(path, target_mnt): 
    from collections import defaultdict
    
    dic_rates = {}
    dic_paths = defaultdict(list)
    with open(path, 'r') as f:
        for line in f: 
            ls_tmp = line[:-1].replace("=", " ").replace(";","").replace(",","").split(' ')
            # print(ls_tmp[1], ls_tmp[5], ls_tmp[10:])
            dic_rates[ls_tmp[1]] = int(ls_tmp[5])
            dic_paths[ls_tmp[1]] += ls_tmp[10:]

    new_dic = {}
    summation = [0]
    def calc(mnt, curr1, curr2, status): 
        # print(mnt)
        if curr2 < curr1: 
            return calc(mnt, curr2, curr1, status)
        tp = tuple(sorted(status))
        if (mnt, curr1, curr2, tp) in new_dic: 
            return new_dic[(mnt, curr1, curr2, tp)]
        if len(status) == len(dic_rates): 
            print('!!')
            val = summation[0]
            new_dic[(mnt, curr1, curr2, tp)] = (target_mnt - mnt) * val
            return (target_mnt - mnt) * val
        else: 
            if mnt == target_mnt: 
                val = summation[0]
                new_dic[(mnt, curr1, curr2, tp)] = val
                return val
            else: 
                val = summation[0]
                res = 0
                if curr1 != curr2: 
                    if curr1 not in status and dic_rates[curr1] > 0 and curr2 not in status and dic_rates[curr2] > 0: 
                        summation[0] += dic_rates[curr1] + dic_rates[curr2]
                        res = max(res, calc(mnt + 1, curr1, curr2, status.union({curr1, curr2})))
                        summation[0] -= dic_rates[curr1] + dic_rates[curr2] 
                    for node1 in dic_paths[curr1]:
                        if curr2 not in status and dic_rates[curr2] > 0: 
                            summation[0] += dic_rates[curr2]
                            res = max(res, calc(mnt + 1, node1, curr2, status.union({curr2})))
                            summation[0] -= dic_rates[curr2]      
                        for node2 in dic_paths[curr2]: 
                            res = max(res, calc(mnt + 1, node1, node2, status.union({})))
                            if node1 == dic_paths[curr1][0] and curr1 not in status and dic_rates[curr1] > 0: 
                                summation[0] += dic_rates[curr1]
                                res = max(res, calc(mnt + 1, curr1, node2, status.union({curr1})))
                                summation[0] -= dic_rates[curr1]
                else: 
                    if curr1 not in status and dic_rates[curr1] > 0: 
                        summation[0] += dic_rates[curr1]
                        res = max(res, calc(mnt + 1, curr1, curr2, status.union({curr1})))
                        summation[0] -= dic_rates[curr1]
                    for i in range(len(dic_paths[curr1])): 
                        node1 = dic_paths[curr1][i]
                        if curr1 not in status and dic_rates[curr1] > 0: 
                            summation[0] += dic_rates[curr1]
                            res = max(res, calc(mnt + 1, curr1, node1, status.union({curr1})))
                            summation[0] -= dic_rates[curr1]
                        for j in range(i, len(dic_paths[curr1])): 
                            node2 = dic_paths[curr1][j]
                            res = max(res, calc(mnt + 1, node1, node2, status.union({})))

                new_dic[(mnt, curr1, curr2, tp)] = val + res
                return val + res
    print(datetime.datetime.now())
    val = calc(0, 'AA', 'AA', set({'AA'}))
    print(val)
    print(datetime.datetime.now())
    return val, new_dic


path1 = 'inputPartial_20221216.txt'
path2 = 'inputFull_20221216.txt'
# part1(path1, 29)
# part1(path2, 29)

# part2(path1, 25)
val, dic = part2(path2, 25)
print(val, len(dic))

# from collections import defaultdict
# dic_rates = {}
# dic_paths = defaultdict(list)
# with open(path2, 'r') as f:
#     for line in f: 
#         ls_tmp = line[:-1].replace("=", " ").replace(";","").replace(",","").split(' ')
#         dic_rates[ls_tmp[1]] = int(ls_tmp[5])
#         dic_paths[ls_tmp[1]] += ls_tmp[10:]
# print(sum(dic_rates.values()))
                    
    
