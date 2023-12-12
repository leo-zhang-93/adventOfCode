# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:06:35 2022

@author: Leo Zhang
"""
# https://adventofcode.com/2022/day/13
def compare(x, y): 
        
    if isinstance(x, int) and isinstance(y, int):  
        if x < y: 
            return 1
        elif x == y: 
            return 0
        else: 
            return -1
    elif isinstance(x, int) and isinstance(y, list): 
        if not y: 
            return -1
        else: 
            plus = 0
            while isinstance(y, list) and len(y) > 0: 
                if len(y) > 1: 
                    plus += 1
                y = y[0]
            if isinstance(y, list) and len(y) == 0: 
                return -1
            else: 
                if x == y: 
                    if plus > 0: 
                        return 1
                    else: 
                        return 0
                elif x < y: 
                    return 1
                else: 
                    return -1
    elif isinstance(y, int) and isinstance(x, list): 
        return -1 * compare(y, x)
    else: 
        idx = 0
        plus = 0
        while idx < len(x) and idx < len(y): 
            xx = x[idx]
            yy = y[idx]
            idx += 1
            val = compare(xx, yy)
            if val == 1: 
                return 1
            elif val == -1: 
                return -1
            else: 
                continue
        if idx == len(x): 
            if idx == len(y): 
                return 0
            else: 
                return 1
        elif idx == len(y): 
            return -1

if __name__ == '__main__': 
    
    """
    path = 'inputFull_20221213.txt'
    res = 0
    with open(path, 'r') as f: 
        tmp_ls = []
        idx = 1
        for line in f:
            if line == '\n': 
                idx += 1
                tmp_ls = []
                continue
            if len(tmp_ls) <= 1: 
                tmp_ls.append(eval(line[:-1]))
            if len(tmp_ls) == 2: 
                # print(tmp_ls[0])
                # print(tmp_ls[1])
                if compare(*tmp_ls) == 1: 
                    # print('!', idx)
                    res += idx
                # print()
            # if idx == 20: 
            #     break
        
    print(res)      
    """
    path = 'inputFull_20221213.txt'
    res = 0
    with open(path, 'r') as f:
        total_lines = 0
        count_top = 0
        count_bottom  = 0
        for line in f: 
            if line == '\n': 
                continue
            else: 
                ls = eval(line[:-1])
                if compare(ls, [[2]]) == 1: 
                    count_top += 1
                elif compare(ls, [[2]])  == 0: 
                    print(2)
                elif compare([[6]], ls) == 1: 
                    count_bottom += 1
                elif compare([[6]], ls) == 0: 
                    print(6)
                total_lines += 1
    print((count_top + 1) * (total_lines + 2 - count_bottom))
                
        