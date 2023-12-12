# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:20:25 2023

@author: Leo Zhang
"""
def part1(path, target):
    ls = []
    with open(path, 'r') as f: 
        for line in f: 
            s1, s2, s3, s4 = line[:-2].split('.')
            tmp_ls = []
            tmp_ls.append(int(s1.split(' ')[-2]))
            tmp_ls.append(int(s2.split(' ')[-2]))
            ls_s3 = s3.split(' ')
            tmp_ls.append(int(ls_s3[-5]))
            tmp_ls.append(int(ls_s3[-2]))
            ls_s4 = s4.split(' ')
            tmp_ls.append(int(ls_s4[-5]))
            tmp_ls.append(int(ls_s4[-2]))
            ls.append([item for item in tmp_ls])
            # print(round(tmp_ls[3] / tmp_ls[2], 2), round(tmp_ls[5] / tmp_ls[4], 2))
    
    n = len(ls)
    result = 0
    for i in range(n): 
        tmp_ls = ls[i]
        c11, c21, c31, c32, c41, c42 = tmp_ls
        status = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        # minute, num of ores, num of clays, num of obsidians, num of ore robots, num of clay robots, num of obisidian robots, geodes broken
        # cnt = [0]
        dic = {}
        def calc(): 
            # cnt[0] += 1
            # print(status)
            tp = tuple(status)
            if tp in dic: 
                return dic[tp]
            if status[0] == target: 
                # print(status)
                dic[tp] = status[7] + status[8]
                return status[7] + status[8]
            if status[1] >= c41 and status[3] >= c42: 
                # tmp_status = [item for item in status]
                status[0] += 1
                status[1] += -c41 + status[4]
                status[2] += status[5]
                status[3] += -c42 + status[6]
                status[8] += status[7]
                status[7] += 1
                res = calc()
                status[7] -= 1
                status[8] -= status[7]
                status[3] -= -c42 + status[6]
                status[2] -= status[5]
                status[1] -= -c41 + status[4]
                status[0] -= 1
                # print(1, tmp_status, status)
                dic[tp] = res
                return res
            res = 0
            if status[1] >= c31 and status[2] >= c32: 
                # tmp_status = [item for item in status]
                status[0] += 1
                status[1] += -c31 + status[4]
                status[2] += -c32 + status[5]
                status[3] += status[6]
                status[8] += status[7]
                status[6] += 1
                res = max(res, calc())
                status[6] -= 1
                status[8] -= status[7]
                status[3] -= status[6]
                status[2] -= -c32 + status[5]
                status[1] -= -c31 + status[4]
                status[0] -= 1
                # print(2, tmp_status, status)
            if status[1] >= c21: 
                # tmp_status = [item for item in status]
                status[0] += 1
                status[1] += -c21 + status[4]
                status[2] += status[5]
                status[3] += status[6]
                status[8] += status[7]
                status[5] += 1
                res = max(res, calc())
                status[5] -= 1
                status[8] -= status[7]
                status[3] -= status[6]
                status[2] -= status[5]
                status[1] -= -c21 + status[4]
                status[0] -= 1
                # print(3, tmp_status, status)
            if status[1] >= c11: 
                # tmp_status = [item for item in status]
                status[0] += 1
                status[1] += -c11 + status[4]
                status[2] += status[5]
                status[3] += status[6]
                status[8] += status[7]
                status[4] += 1
                res = max(res, calc())
                status[4] -= 1
                status[8] -= status[7]
                status[3] -= status[6]
                status[2] -= status[5]
                status[1] -= -c11 + status[4]
                status[0] -= 1
                # print(4, tmp_status, status)
            # tmp_status = [item for item in status]
    
            status[0] += 1
            status[1] += status[4]
            status[2] += status[5]
            status[3] += status[6]
            status[8] += status[7]
            res = max(res, calc())
            status[8] -= status[7]
            status[3] -= status[6]
            status[2] -= status[5]
            status[1] -= status[4]
            status[0] -= 1
                # print(5, tmp_status, status)
            dic[tp] = res
            return res
        
        res = calc()
        print(i + 1, res)
        result += (i + 1) * res
    
    return result

def part2(path, target): 
    ls = []
    import datetime
    with open(path, 'r') as f: 
        for line in f: 
            s1, s2, s3, s4 = line[:-2].split('.')
            tmp_ls = []
            tmp_ls.append(int(s1.split(' ')[-2]))
            tmp_ls.append(int(s2.split(' ')[-2]))
            ls_s3 = s3.split(' ')
            tmp_ls.append(int(ls_s3[-5]))
            tmp_ls.append(int(ls_s3[-2]))
            ls_s4 = s4.split(' ')
            tmp_ls.append(int(ls_s4[-5]))
            tmp_ls.append(int(ls_s4[-2]))
            ls.append([item for item in tmp_ls])
            # print(round(tmp_ls[3] / tmp_ls[2], 2), round(tmp_ls[5] / tmp_ls[4], 2))
    
    n = len(ls)
    print(n)
    
    result = 0
    for i in range(3): 
        now = datetime.datetime.now()
        print(now.strftime("%m/%d/%Y %H:%M:%S"))
        tmp_ls = ls[i]
        c11, c21, c31, c32, c41, c42 = tmp_ls
        dic = {}
        def calc(minute, a1, a2, a3, b1, b2, b3, b4): 
            tp = (minute, a1, a2, a3, b1, b2, b3, b4)
            # print(tp)
            if tp in dic: 
                return dic[tp]
            if minute == target: 
                dic[tp] = b4
                return b4
            if a1 >= c41 and a3 >= c42: 
                # tmp_status = [item for item in status]
                res = calc(
                    minute + 1, 
                    a1 - c41 + b1, 
                    a2 + b2, 
                    a3 - c42 + b3,
                    b1, 
                    b2, 
                    b3, 
                    b4 + 1,                 
                    ) + b4
                dic[tp] = res
                return res
            res = b4
            if a1 >= c31 and a2 >= c32: 
                res = max(res, calc(
                    minute + 1, 
                    a1 - c31 + b1, 
                    a2 - c32 + b2, 
                    a3 + b3,
                    b1, 
                    b2, 
                    b3 + 1, 
                    b4,                 
                    ) + b4
                    )
            if a1 >= c21: 
                res = max(res, calc(
                    minute + 1, 
                    a1 - c21 + b1, 
                    a2 + b2, 
                    a3 + b3,
                    b1, 
                    b2 + 1, 
                    b3, 
                    b4,                 
                    ) + b4
                    )
            if a1 >= c11: 
                res = max(res, calc(
                    minute + 1, 
                    a1 - c11 + b1, 
                    a2 + b2, 
                    a3 + b3,
                    b1 + 1, 
                    b2, 
                    b3, 
                    b4,                 
                    ) + b4
                    )
            res = max(res, calc(
                minute + 1, 
                a1 + b1, 
                a2 + b2, 
                a3 + b3,
                b1, 
                b2, 
                b3, 
                b4,                 
                ) + b4
                )
            dic[tp] = res
            return res
        res = calc(0, 0, 0, 0, 1, 0, 0, 0)
        print(i + 1, res)
        print(len(dic))
        result += (i + 1) * res
        now = datetime.datetime.now()
        print(now.strftime("%m/%d/%Y %H:%M:%S"))
        print()
    
    return result
    
path1 = 'inputPartial_20221219.txt'
path2 = 'inputFull_20221219.txt'

target1 = 23
target2 = 31

part1(path1, target1)
part1(path2, target1)

part2(path2, target2)
    
    
            
            
        
        