# Arrived at hotel from Lotus's a bit later than problem open time
# The second part is very annoying as there's almost on info on how the Xmas tree looks like
# First, I thought the top middle cell would be occupied by an * if it's a tree and tried
# But cannot find a solution
# Then, I thought maybe the bottom line of the tree would contain quite a few continuous *s
# and I used 30 as a rule of thumb and print out the grid and find.
# There should be of no better solution if you don't know the exact shape of the tree

def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                pos, vel = line[:-1].split(' ')
                px, py = pos[2:].split(',')
                vx, vy = vel[2:].split(',')
                ls.append([int(py), int(px), int(vy), int(vx)])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def calc(px, py, vx, vy, m, n, times):
    fpx = px + vx * times
    fpy = py + vy * times
    return fpx % m, fpy % n

def check1(ls):
    res = [0] * 4
    m = 103
    n = 101
    for px, py, vx, vy in ls:
        newx, newy = calc(px, py, vx, vy, m, n, 100)
        if newx <= m // 2 - 1:
            if newy <= n // 2 - 1:
                res[0] += 1
            elif newy >= n // 2 + 1:
                res[1] += 1
        elif newx >= m // 2 + 1:
            if newy <= n // 2 - 1:
                res[2] += 1
            elif newy >= n // 2 + 1:
                res[3] += 1
    init = 1
    for i in range(4):
        init *= res[i]
    return init

def check2(ls):
    m = 103
    n = 101
    from collections import defaultdict
    for times in range(1, 10000):
        grid = [['-'] * n for _ in range(m)]
        dic = defaultdict(set)
        flag = 0
        for px, py, vx, vy in ls:
            newx, newy = calc(px, py, vx, vy, m, n, times)
            grid[newx][newy] = '*'
            dic[newx].add(newy)
            if len(dic[newx]) >= 30:
                flag = 1
        if flag == 1:
            print(times)
            for subls in grid:
                print(''.join(subls))
        flag = 0

if __name__ == "__main__":
    path1 = 'inputFull_20241214.txt'
    # path1 = 'inputPartial_20241214.txt'
    ls = getList(path1)
    print(f"Part 1: {check1(ls)}")
    check2(ls)





