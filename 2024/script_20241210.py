# Vacation@Phuket 2024.12.10
def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(list(map(int, line[:-1])))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def calc1(ls):
    m, n = len(ls), len(ls[0])
    ls_zeroes = []
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 0:
                ls_zeroes.append([i, j])
    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    def calc(i, j):
        queue = [[i, j]]
        tmp = []
        level = 0
        seen = set()
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < m and 0 <= yy < n and ls[xx][yy] == level + 1:
                    if (xx, yy) not in seen:
                        tmp.append([xx, yy])
                        seen.add((xx, yy))
            if not queue:
                if level == 8:
                    return len(seen)
                else:
                    queue = tmp
                    tmp = []
                    level += 1
                    seen = set()
    res = 0
    for x, y in ls_zeroes:
        res += calc(x, y)
    return res

def calc2(ls):
    m, n = len(ls), len(ls[0])
    ls_zeroes = []
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 0:
                ls_zeroes.append([i, j])
    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    def calc(i, j):
        queue = [[i, j]]
        tmp = []
        level = 0
        dic = {(i, j): 1}
        newdic = {}
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < m and 0 <= yy < n and ls[xx][yy] == level + 1:
                    if (xx, yy) not in newdic:
                        tmp.append([xx, yy])
                        newdic[(xx, yy)] = dic[(x, y)]
                    else:
                        newdic[(xx, yy)] += dic[(x, y)]
            if not queue:
                if level == 8:
                    return sum(newdic.values())
                else:
                    queue = tmp
                    tmp = []
                    level += 1
                    dic = newdic.copy()
                    newdic = {}
    res = 0
    for x, y in ls_zeroes:
        res += calc(x, y)
    return res

if __name__ == "__main__":
    path1 = 'inputFull_20241210.txt'
    # path1 = 'inputPartial_20241210.txt'
    ls = getList(path1)
    print(f"Part 1: {calc1(ls)}")
    print(f"Part 2: {calc2(ls)}")