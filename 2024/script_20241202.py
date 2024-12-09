def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append([item for item in map(int, line[:-1].split(' '))])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls


def check1(ls):
    increase = True
    if ls[1] < ls[0]:
        increase = False
    n = len(ls)
    for i in range(1, n):
        diff = ls[i] - ls[i - 1]
        if (increase and 1 <= diff <= 3) or (not increase and -3 <= diff <= -1):
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    path1 = 'inputPartial_20241202.txt'
    # path1 = 'inputFull_20241202.txt'
    ls = getList(path1)

    # Part 1
    res1 = 0
    for item in ls:
        if check1(item):
            res1 += 1
    print(res1)

    # Part 2
    res2 = 0
    for item in ls:
        lenitem = len(item)
        for j in range(lenitem):
            if check1(item[:j] + item[j + 1:]):
                # print(item, item[:lenitem] + item[lenitem + 1:])
                res2 += 1
                break
    print(res2)
