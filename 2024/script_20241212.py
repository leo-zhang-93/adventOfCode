# @Phi Phi Island D.M.C Restaurant
def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(list(line[:-1]))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def check1(ls):

    def calc1(i, j):
        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
        ]
        val = ls[i][j]
        queue = [[i, j]]
        seen = set([(i, j)])
        big_seen.add((i, j))
        area = 1
        peri = 0
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < m and 0 <= yy < n and ls[xx][yy] == val and (xx, yy) not in seen:
                    area += 1
                    queue.append([xx, yy])
                    seen.add((xx, yy))
                    big_seen.add((xx, yy))
                elif (not (0 <= xx < m and 0 <= yy < n)) or ls[xx][yy] != val:
                    peri += 1
        return area, peri

    m, n = len(ls), len(ls[0])
    big_seen = set()
    res = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in big_seen:
                a, p = calc1(i, j)
                res += a * p
    return res

def check2(ls):

    def calc2(i, j):
        # this one is derived from calc1
        # just need to keep in mind
        # 1) give the borders coordinates, separately for horizontal and vetical ones
        # sort them also separately and check whether any are connected
        # 2) the example with a cross is helpful.
        # two connected borders are associated with four tiles, two on each side of the borders
        # we need to make sure at least one side share the same type.
        # otherwise, the borders are not connected.
        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
        ]
        val = ls[i][j]
        queue = [[i, j]]
        seen = set([(i, j)])
        big_seen.add((i, j))
        area = 1
        peri = 0
        ls_peri_h = []
        ls_peri_v = []
        while queue:
            x, y = queue.pop(0)
            for idx, [dx, dy] in enumerate(directions):
                xx = x + dx
                yy = y + dy
                if 0 <= xx < m and 0 <= yy < n and ls[xx][yy] == val and (xx, yy) not in seen:
                    area += 1
                    queue.append([xx, yy])
                    seen.add((xx, yy))
                    big_seen.add((xx, yy))
                elif (not (0 <= xx < m and 0 <= yy < n)) or ls[xx][yy] != val:
                    peri += 1
                    if idx == 0:
                        ls_peri_h.append([x, y])
                    elif idx == 1:
                        ls_peri_h.append([xx, yy])
                    elif idx == 2:
                        ls_peri_v.append([x, y])
                    else:
                        ls_peri_v.append([xx, yy])
        ls_peri_h = sorted(ls_peri_h) + [[float('inf'), float('inf')]]
        ls_peri_v = sorted(ls_peri_v, key=lambda x: [x[1], x[0]]) + [[float('inf'), float('inf')]]
        lenh = len(ls_peri_h)
        lenv = len(ls_peri_v)
        peri_h = 0
        peri_v = 0
        for i in range(1, lenh):
            x, y = ls_peri_h[i]
            prevx, prevy = ls_peri_h[i - 1]
            if x != prevx or y != prevy + 1:
                peri_h += 1
            else:
                if x == 0 or x == m:
                    continue
                else:
                    if (ls[x - 1][prevy] == val and ls[x][y] == val) or (ls[x][prevy] == val and ls[x - 1][y] == val):
                        peri_h += 1
        for i in range(1, lenv):
            x, y = ls_peri_v[i]
            prevx, prevy = ls_peri_v[i - 1]
            if y != prevy or x != prevx + 1:
                peri_v += 1
            else:
                if y == 0 or y == n:
                    continue
                else:
                    if (ls[prevx][y - 1] == val and ls[x][y] == val) or (ls[prevx][y] == val and ls[x][y - 1] == val):
                        peri_v += 1
        return area, peri_h, peri_v

    m, n = len(ls), len(ls[0])
    big_seen = set()
    res = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in big_seen:
                a, p1, p2 = calc2(i, j)
                res += a * (p1 + p2)
    return res

if __name__ == "__main__":
    # path1 = 'inputFull_20241212.txt'
    path1 = 'inputPartial_20241212.txt'
    ls = getList(path1)
    print(f"Part 1: {check1(ls)}")
    print(f"Part 2: {check2(ls)}")





