# -*- coding: utf-8 -*-
"""
Created on Wed Dec 01 15:40:01 2023

@author: Leo Zhang
"""

def calc1(path):
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            l = ''
            r = ''
            for char in line: 
                if 48 <= ord(char) <= 57:
                    if l == '': 
                        l = char
                    r = char
            res += int(l + r)
    return res

def calc2(path): 
    res = 0
    with open(path, 'r') as f:
        for line in f: 
            l = ''
            r = ''
            for i in range(len(line)): 
                char = line[i]
                if 48 <= ord(char) <= 57:
                    if l == '': 
                        l = char
                    r = char
                else: 
                    yn, val = check(line, i)
                    if yn: 
                        if l == '': 
                            l = val
                        r = val
            res += int(l + r)
    return res

def check(string, idx): 
    ls = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(9): 
        item = ls[i]
        length = len(item)
        if string[idx:(idx + length)] == item: 
            return True, str(i + 1)
    return False, None

def main(path):
    a = calc1(path)
    b = calc2(path)
    print(f'answer 1 - {a}')
    print(f'answer 2 - {b}')

if __name__ == '__main__':
    path = 'inputPartial_20231201.txt'
    main(path)