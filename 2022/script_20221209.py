# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 23:44:30 2022

@author: Leo Zhang
"""

def part1(path):
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            direction, steps = line[:-1].split(' ')
            steps = int(steps)
            ls.append([direction, steps])
    
    xh = 0
    yh = 0
    xt = 0
    yt = 0
    seen = set([(xt, yt)])
    for direction, steps in ls: 
        if direction == 'R': 
            for i in range(steps): 
                if yt == yh: 
                    if xt < xh: 
                        xt += 1
                elif yt < yh: 
                    if xt < xh: 
                        xt += 1
                        yt += 1
                else: 
                    if xt < xh:
                        xt += 1
                        yt -= 1
                seen.add((xt, yt))
                xh += 1

        elif direction == 'L': 
            for i in range(steps): 
                if yt == yh: 
                    if xt > xh: 
                        xt -= 1
                elif yt < yh: 
                    if xt > xh: 
                        xt -= 1
                        yt += 1
                else: 
                    if xt > xh: 
                        xt -= 1
                        yt -= 1
                seen.add((xt, yt))
                xh -= 1

        elif direction == 'U': 
            for i in range(steps): 
                if xt == xh: 
                    if yt < yh: 
                        yt += 1
                elif xt < xh: 
                    if yt < yh: 
                        yt += 1
                        xt += 1
                else: 
                    if yt < yh: 
                        yt += 1
                        xt -= 1
                seen.add((xt, yt))
                yh += 1
        else: 
            for i in range(steps): 
                if xt == xh: 
                    if yt > yh: 
                        yt -= 1
                elif xt < xh: 
                    if yt > yh: 
                        yt -= 1
                        xt += 1
                else: 
                    if yt > yh: 
                        yt -= 1
                        xt -= 1
                seen.add((xt, yt))
                yh -= 1    
    
    return len(seen)

def part2(path):
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            direction, steps = line[:-1].split(' ')
            steps = int(steps)
            ls.append([direction, steps])
    # print(ls)
    seen = set([(0, 0)])
    def calc(dxh, dyh, rx, ry):
        if abs(rx) + abs(ry) == 0: 
            return 0, 0
        if abs(dxh) + abs(dyh) == 0: 
            return 0, 0
        if abs(rx) + abs(ry) == 1: 
            p = dxh * rx + dyh * ry
            if p >= 0: 
                return 0, 0
            else: 
                return dxh, dyh
        else: 
            p = dxh * rx + dyh * ry
            if p >= 1: 
                return 0, 0
            elif p == 0: 
                if dxh == rx: 
                    return 0, dyh
                else: 
                    return dxh, 0
            else: 
                return -rx, -ry            
    
    seen = set([(0, 0)])
    ls_nodes = [[0, 0] for _ in range(10)]
    for direction, steps in ls: 
        # print(direction, steps)
        for _ in range(steps):
            if direction == 'L': 
                dx, dy = -1, 0
            elif direction == 'R': 
                dx, dy = 1, 0
            elif direction == 'U': 
                dx, dy = 0, 1
            else: # D
                dx, dy = 0, -1
                
            for i in range(10 - 1): 
                rx = ls_nodes[i + 1][0] - ls_nodes[i][0]
                ry = ls_nodes[i + 1][1] - ls_nodes[i][1]
                newdx, newdy = calc(dx, dy, rx, ry)
                ls_nodes[i][0] += dx
                ls_nodes[i][1] += dy
                dx, dy = newdx, newdy
            ls_nodes[-1][0] += dx
            ls_nodes[-1][1] += dy
            seen.add((ls_nodes[-1][0], ls_nodes[-1][1]))  
            # print(ls_nodes)
        # print()
    return len(seen)

path1 = 'inputPartial_20221209.txt'
path3 = 'inputPartial_20221209_01.txt'
path2 = 'inputFull_20221209.txt'

# print(part1(path1))
# print(part1(path2))
print(part2(path3))
print(part2(path2))
    
        