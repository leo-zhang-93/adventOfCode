def getList(path):
    ls1 = []
    ls2 = []
    try:
        flag = 0
        with open(path, 'r') as f:
            for line in f:
                if line == '\n':
                    flag = 1
                    continue
                if flag == 0:
                    ls1.append(line[:-1])
                else:
                    ls2.append(line[:-1])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return [], []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []

    return ls1, ls2


def check1(ls1, ls2):
    from collections import defaultdict
    dic = defaultdict(set)
    for val1, val2 in ls1:
        dic[val1].add(val2)
    res = 0
    for subls in ls2:
        flag = 0
        n = len(subls)
        for i in range(n - 1):
            val1 = subls[i]
            for j in range(i + 1, n):
                val2 = subls[j]
                if val1 in dic[val2]:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            res += subls[n // 2]
    return res


def check2(ls1, ls2):
    from collections import defaultdict
    dic = defaultdict(set)
    for val1, val2 in ls1:
        dic[val1].add(val2)
    res = 0
    for idx, subls in enumerate(ls2):
        while True:
            flag = 0
            n = len(subls)
            for i in range(n - 1):
                val1 = subls[i]
                for j in range(i + 1, n):
                    val2 = subls[j]
                    if val1 in dic[val2]:
                        subls[i], subls[j] = subls[j], subls[i]
                        flag = 1
            if flag == 0:
                res += subls[n // 2]
                break
    return res


if __name__ == "__main__":
    path1 = 'inputFull_20241205.txt'
    # path1 = 'inputPartial_20241205.txt'
    ls1, ls2 = getList(path1)
    ls1_ = [list(map(int, item.split('|'))) for item in ls1]
    ls2_ = [list(map(int, item.split(','))) for item in ls2]

    # Part 1:
    res1 = check1(ls1_, ls2_)
    print(f"Part 1: {res1}")

    # Part 2:
    res2 = check2(ls1_, ls2_)
    print(f"Part 2: {res2 - res1}")
