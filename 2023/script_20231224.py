# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:38:28 2023

@author: Leo Zhang
"""
import numpy as np
path = 'inputPartial_20231224.txt'
grid = []
with open(path, 'r') as f:
    for line in f:
        pos, vel = line[:-1].split(' @ ')
        px, py, pz = pos.split(', ')
        vx, vy, vz = vel.split(', ')
        grid.append(list(map(int, [px, py, pz, vx, vy, vz])))

m = len(grid)
def check_intersect(x1, y1, vx1, vy1, x2, y2, vx2, vy2): 
    if vx1 == vx2 == 0: 
        return False, None, None
    else: 
        if vy1 / vx1 == vy2 / vx2: 
            return False, None, None
        else: 
            s1 = vy1 / vx1
            s2 = vy2 / vx2
            resx = (s1 * x1 - s2 * x2 + y2 - y1) / (s1 - s2)
            resy = (s1 * s2 * x1 - s1 * s2 * x2 + s1 * y2 - s2 * y1) / (s1 - s2)
            if (resx - x1) * vx1 + (resy - y1) * vy1 >= 0 and (resx - x2) * vx2 + (resy - y2) * vy2 >= 0: 
                return True, resx, resy
            return False, resx, resy

res = 0
lb = 200000000000000
ub = 400000000000000
for i in range(m - 1): 
    x1, y1, _, vx1, vy1, _ = grid[i]
    for j in range(i + 1, m): 
        x2, y2, _, vx2, vy2, _ = grid[j]
        tf, resx, resy = check_intersect(x1, y1, vx1, vy1, x2, y2, vx2, vy2)
        if tf and lb <= resx <= ub and lb <= resy <= ub: 
            res += 1
            # print(grid[i], grid[j], resx, resy)
print('solution of part 1:', res)
print()

## take the first 3 as example for part 2. 

x1, y1, z1, vx1, vy1, vz1 = grid[0]
x2, y2, z2, vx2, vy2, vz2 = grid[1]
x3, y3, z3, vx3, vy3, vz3 = grid[2]

## Assume the time used by the target hailstone from initial point to reach ex 1, ex 2, & ex 3 (they are moving as well) are t1, t2, & t3. 
## the distances between ex1, ex2, and ex3 (as of reached by the target hailstone) should be proportional to (t2 - t1) and (t3 - t2)
## the equations would be 
## (x3 - x2 + vx3 * t3 - vx2 * t2) / (x2 - x1 + vx2 * t2 - vx1 * t1) = (t3 - t2) / (t2 - t1)
## after transformation: (vx3 - vx2) t2 t3 + (vx2 - vx1) t1 t2 + (vx1 - vx3) t1 t2 + (x3 - x1) t2 + (x2 - x3) t1 + (x1 - x2) t3 = 0
## same for y and z. 
## this function is to get the coefficients. 
def calc(v1, v2, v3, a1, a2, a3): 
    return v3 - v2, v2 - v1, v1 - v3, a3 - a1, a2 - a3, a1 - a2

print('Coefficients')
coef1 = calc(vx1, vx2, vx3, x1, x2, x3)
coef2 = calc(vy1, vy2, vy3, y1, y2, y3)
coef3 = calc(vz1, vz2, vz3, z1, z2, z3)
print(coef1)
print(coef2)
print(coef3)
print()

### we can elimated the 2nd order items
# below are the multipliers for each equation. We add up the multiplied equations and can elimate the 2nd order items. 
# should have a function to solve those. 
m1 = 31071
m2 = -12201
m3 = 22930

print('New Coefficients!')
# coef for t2, t1, and t3!!
newcoef = m1 * coef1[3] + m2 * coef2[3] + m3 * coef3[3], m1 * coef1[4] + m2 * coef2[4] + m3 * coef3[4], m1 * coef1[5] + m2 * coef2[5] + m3 * coef3[5]
print(newcoef)
print()

## put the ratio between (t3 - t2) over (t2 - t1) back to the euquation for the solutions. 
## (t3 - t2)/(t2 - t1)  = k2 / k1
k1 = -newcoef[2]
k2 = -newcoef[1]

## this function gives the coef for t1, t2, t3 and 1. 
def calc_coef(k1, k2, v1, v2, v3, var1, var2, var3): 
    return k2 * v1, -(k1 * v2 + k2 * v2), k1 * v3, k1 * (var3 - var2) - k2 * (var2 - var1)

finalcoef_x = calc_coef(k1, k2, vx1, vx2, vx3, x1, x2, x3)
finalcoef_y = calc_coef(k1, k2, vy1, vy2, vy3, y1, y2, y3)
finalcoef_z = calc_coef(k1, k2, vz1, vz2, vz3, z1, z2, z3)
print('Final Coefficents!')
print(finalcoef_x)
print(finalcoef_y)
print(finalcoef_z)
print()

### solved using this site. 
# Should reuse the solving funtions to be created above.
t1 = 130621773037
t2 = 423178590960
t3 = 631793973864

## test if it's corrected. 
print('Test equation LHS value:', t1 * finalcoef_x[0] + t2 * finalcoef_x[1] + t3 * finalcoef_x[2] + finalcoef_x[3])
print()
print('t1', x1 + a1 * vx1, y1 + a1 * vy1, z1 + a1 * vz1)  
print('t2', x2 + a2 * vx2, y2 + a2 * vy2, z2 + a2 * vz2)  
print('t3', x3 + a3 * vx3, y3 + a3 * vy3, z3 + a3 * vz3) 
print()

print('test divided', (x2 + a2 * vx2 - (x1 + a1 * vx1)) % (a2 - a1), (y2 + a2 * vy2 - (y1 + a1 * vy1)) % (a2 - a1), (z2 + a2 * vz2 - (z1 + a1 * vz1)) % (a2 - a1))
print()

## get pace of the 3 dimensions
pacex = (x2 + a2 * vx2 - (x1 + a1 * vx1)) // (a2 - a1)
pacey = (y2 + a2 * vy2 - (y1 + a1 * vy1)) // (a2 - a1)
pacez = (z2 + a2 * vz2 - (z1 + a1 * vz1)) // (a2 - a1)
print(pacex, pacey, pacez)

x0, y0, z0 = x1 + a1 * vx1 - a1 * pacex, y1 + a1 * vy1 - a1 * pacey, z1 + a1 * vz1 - a1 * pacez
print()
print('Test t2', x0 + pacex * a2, y0 + pacey * a2, z0 + pacez * a2)
print()
print('initial start point', x1 + a1 * vx1 - a1 * pacex, y1 + a1 * vy1 - a1 * pacey, z1 + a1 * vz1 - a1 * pacez)
print('Result of Part 2:', sum([x1 + a1 * vx1 - a1 * pacex, y1 + a1 * vy1 - a1 * pacey, z1 + a1 * vz1 - a1 * pacez]))
