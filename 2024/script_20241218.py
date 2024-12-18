# @Phi Phi Island D.M.C Restaurant
def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(list(map(int, line[:-1].split(','))))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def calc1(ls, m, n, uptoidx):
    grid = [['.'] * n for _ in range(m)]
    for i in range(uptoidx):
        x, y = ls[i]
        grid[x][y] = '#'
    queue = [[0, 0]]
    seen = set([(0, 0)])
    tmp = []
    level = 1
    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    flag = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen and grid[xx][yy] != '#':
                tmp.append([xx, yy])
                seen.add((xx, yy))
                if xx == m - 1 and yy == n - 1:
                    return level
                    flag = 1
                    break
        if flag == 1:
            break
        if not queue:
            queue = tmp
            tmp = []
            level += 1

def calc2(ls, m, n, uptoidx):
    grid = [['.'] * n for _ in range(m)]
    for i in range(uptoidx):
        x, y = ls[i]
        grid[x][y] = '#'
    for idx in range(uptoidx, len(ls)):
        x, y = ls[idx]
        grid[x][y] = '#'
        queue = [[0, 0]]
        seen = set([(0, 0)])
        tmp = []
        level = 1
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        flag = 0
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen and grid[xx][yy] != '#':
                    tmp.append([xx, yy])
                    seen.add((xx, yy))
                    if xx == m - 1 and yy == n - 1:
                        flag = 1
                        break
            if flag == 1:
                break
            if not queue:
                if not tmp:
                    return ls[idx]
                queue = tmp
                tmp = []
                level += 1

if __name__ == "__main__":
    path1 = 'inputFull_20241218.txt'
    # path1 = 'inputPartial_20241218.txt'
    ls = getList(path1)
    m, n = 71, 71
    uptoidx1 = 1024
    uptoidx2 = 2900
    print(f"Part 1: {calc1(ls, m, n, uptoidx1)}")
    print(f"Part 2: {','.join(map(str, calc2(ls, m, n, uptoidx2)))}")