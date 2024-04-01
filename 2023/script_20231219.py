# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:57:11 2023

@author: Leo Zhang
"""
import copy
path = 'inputPartial_20231219.txt'
ls_rules = []
ls_ratings = []
dic = {}
with open(path, 'r') as f:
    flag = 0
    for line in f:
        if line == '\n': 
            flag = 1
            continue
        if flag == 0: 
            name, rule = line[:-2].split('{')
            rule = rule.replace(';', ',').replace(':', ',').split(',')
            dic[name] = rule
            ls_rules.append([name, rule])
        else: 
            string = line[1:-2]
            newstring = string.split(',')
            values = [int(item.split('=')[1]) for item in newstring]
            ls_ratings.append(values)

#xmas
# print(len(ls_rules))
# print(ls_rules)
# print(len(ls_ratings))
# print(ls_ratings[0])
# print(dic['in'])

def calc(values, rule): 
    x, m, a, s = values
    return eval(rule)

res = []
result = 0
nratings = len(ls_ratings)
for i in range(nratings): 
    rat = ls_ratings[i]
    name = 'in'
    rule = dic[name]
    # print(name, rule)
    flag = 0
    while True: 
        length = len(rule)
        idx = 0
        while True:
            rl = rule[idx]
            # print(rl)
            if rl == 'A': 
                res.append(i)
                result += sum(ls_ratings[i])
                flag = 1
                break
            elif rl == 'R': 
                flag = 1
                break
            elif rl in dic: 
                name = rl
                # print(name)
                rule = dic[name]
                break
            else: 
                if calc(rat, rl): 
                    idx += 1
                else: 
                    idx += 2
        if flag == 1: 
            break
# print(res)
# print(result)

dic_chars = {'x': 0, 'm': 1, 'a': 2, 's': 3}

dic_res = {}

def cross(ls1, ls2): 
    # print(ls1, ls2)
    res = []
    for i in range(len(ls1)): 
        for j in range(len(ls2)):
            tmp = [[1, 4000] for _ in range(4)]
            flag = 0
            for c in range(4): 
                for s in range(2): 
                    if s == 0:
                        tmp[c][s] = max(ls1[i][c][s], ls2[j][c][s], tmp[c][s])
                    else: 
                        tmp[c][s] = min(ls1[i][c][s], ls2[j][c][s], tmp[c][s])
                        if tmp[c][s] < tmp[c][s - 1]: 
                            flag = 1
                            break
                if flag == 1: 
                    break
            if flag != 1: 
                res.append(tmp)
    return res

def add_conditions(ls, string, tf): 
    ls = copy.deepcopy(ls)
    char = string[0]
    sgn = string[1]
    val = int(string[2:])
    for j in range(len(ls)): 
        if sgn == '>':
            if tf == True: 
                ls[j][dic_chars[char]][0] = max(ls[j][dic_chars[char]][0], val + 1)
            else: 
                ls[j][dic_chars[char]][1] = min(ls[j][dic_chars[char]][1], val)
        else: 
            if tf == True: 
                ls[j][dic_chars[char]][1] = min(ls[j][dic_chars[char]][1], val - 1)
            else: 
                ls[j][dic_chars[char]][0] = max(ls[j][dic_chars[char]][0], val)
    return ls
    
def calc2(rule_name): 
    if rule_name in dic_res: 
        return dic_res[rule_name]
    else: 
        res = []
        rule = dic[rule_name]
        length = len(rule)
        lmts_t = [[[1, 4000] for _ in range(4)]]
        lmts_f = [[[1, 4000] for _ in range(4)]]
        for i in range(length): 
            rl = rule[i]
            if i == 0: 
                lmts_t = add_conditions(lmts_t, rl, True)
                lmts_f = add_conditions(lmts_f, rl, False)
                print(rule_name, lmts_t)
                print(rule_name, lmts_f)
            else: 
                if i % 2 == 1: 
                    # True
                    if rl == 'A': 
                        res += lmts_t.copy()
                    elif rl == 'R': 
                        continue
                    else: 
                        res_prev = calc2(rl)
                        # print('!1', rl)
                        res += cross(lmts_t, res_prev)
                else: 
                    # False
                    if rl == 'A': 
                        res += copy.deepcopy(lmts_f)
                        # print('!!!')
                    elif rl == 'R': 
                        continue
                    elif rl in dic: 
                        res_prev = calc2(rl)
                        # print('!2')
                        res += cross(lmts_f, res_prev)
                    else: 
                        print('!0', rule_name, lmts_f)
                        lmts_t = add_conditions(lmts_f, rl, True)
                        print('!1', rule_name, lmts_f)
                        lmts_f = add_conditions(lmts_f, rl, False)
                        print(rule_name, lmts_t)
                        print('!2', rule_name, lmts_f)
        dic_res[rule_name] = res
        return res

calc2('in')

result = 0
for ls in dic_res['in']: 
    print(ls)
    tmp_res = 1
    for x1, x2 in ls: 
        tmp_res *= (x2 - x1 + 1)
    print(tmp_res)
    result += tmp_res
print(result)
            
            
            
        



        
            
            
            