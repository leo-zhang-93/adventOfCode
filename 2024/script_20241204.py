def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(line[:-1])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def check1(x, y):
    res = 0
    lsxmas = 'XMAS'
    directions = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0],
        [1, 1],
        [-1, -1],
        [1, -1],
        [-1, 1]
    ]
    for dx, dy in directions:
        flag = 0
        for idx in range(4):
            xx = x + dx * idx
            yy = y + dy * idx
            if not (0 <= xx < m and 0 <= yy < n):
                flag = 1
                break
            elif ls[xx][yy] != lsxmas[idx]:
                flag = 1
                break
        if flag == 0:
            res += 1
    return res

def check2(x, y):
    res = 0
    ls_ms = 'MS'
    directions = [
        [-1, -1, 1, 1],
        [-1, 1, 1, -1]
    ]
    flag = 0
    for dx1, dy1, dx2, dy2 in directions:
        xx1, yy1 = x + dx1, y + dy1
        xx2, yy2 = x + dx2, y + dy2
        if 0 <= xx1 < m and 0 <= yy1 < n and 0 <= xx2 < m and 0 <= yy2 < n and ((ls[xx1][yy1] == 'M' and ls[xx2][yy2] == 'S') or (ls[xx1][yy1] == 'S' and ls[xx2][yy2] == 'M')):
            continue
        else:
            flag = 1
            break
    if flag == 0:
        return 1
    return 0

if __name__ == "__main__":
    path1 = 'inputFull_20241204.txt'
    # path1 = 'inputPartial_20241204.txt'
    ls = getList(path1)
    m = len(ls)
    n = len(ls[0])
    res1 = 0
    res2 = 0
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 'X':
                res1 += check1(i, j)
            if ls[i][j] == 'A':
                res2 += check2(i, j)
    print(res1)
    print(res2)

