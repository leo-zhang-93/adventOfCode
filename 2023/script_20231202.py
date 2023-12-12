# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:09:33 2023

@author: Leo Zhang
"""

path = 'inputPartial_20231202.txt'

ls_constants1 = [12, 13, 14]

def calc1(path): 
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            game, results = line[:-1].split(': ')
            gamenum = int(game[5:])
            #print(f'!{gamenum}')
            results_ = results.split('; ')
            flag = 0
            for result in results_: 
                ls = [0] * 3 # r g b
                for item in result.split(', '):           
                    if item[-3:] == 'red': 
                        ls[0] = int(item[:-4])
                    elif item[-5:] == 'green':
                        ls[1] = int(item[:-6])
                    elif item[-4:] == 'blue': 
                        ls[2] = int(item[:-5])
                #print(ls)
                if ls[0] <= ls_constants1[0] and ls[1] <= ls_constants1[1] and ls[2] <= ls_constants1[2]: 
                    flag = 0
                else: 
                    flag = 1
                    break
            if flag == 0: 
                #print('!!!')
                res += gamenum
            #print()
        return res

print(calc1(path))

def calc2(path): 
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            game, results = line[:-1].split(': ')
            results_ = results.split('; ')
            flag = 0
            ls = [0] * 3 # r g b
            for result in results_: 
                for item in result.split(', '):           
                    if item[-3:] == 'red': 
                        ls[0] = max(ls[0], int(item[:-4]))
                    elif item[-5:] == 'green':
                        ls[1] = max(ls[1], int(item[:-6]))
                    elif item[-4:] == 'blue': 
                        ls[2] = max(ls[2], int(item[:-5]))
            res += ls[0] * ls[1] * ls[2]
        return res

print(calc2(path))
                
                    
            