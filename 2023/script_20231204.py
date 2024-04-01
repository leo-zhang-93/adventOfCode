# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 13:01:45 2023

@author: Leo Zhang
"""

def tomatrix(path):
    ls = []
    with open(path, 'r') as f:
        for line in f:
            p1, p2 = line[10:-1].strip().split(' | ')
            ls.append([[int(item) for item in p1.strip().split(' ') if item], [int(item) for item in p2.strip().split(' ') if item]])
    return ls

def part1(path):
    ls = tomatrix(path)
    res = 0
    for p1, p2 in ls:
        wins = len(set(p1).intersection(set(p2)))
        if wins:
            res += 2 ** (wins - 1)
    return res

def part2(path):
    ls = tomatrix(path)
    n = len(ls)
    ls_cards = [1] * n
    res = 0
    for i in range(n):
        counti = ls_cards[i]
        res += counti
        p1, p2 = ls[i]
        wins = len(set(p1).intersection(set(p2)))
        if wins:
            for j in range(i + 1, i + wins + 1):
                ls_cards[j] += ls_cards[i]
    return res

def main(path):
    print(part1(path))
    print(part2(path))

if __name__ == '__main__':
    path = 'inputPartial_20231204.txt'
    main(path)