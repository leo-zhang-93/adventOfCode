# @On the boat from Phi Phi back to Phuket
def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            tmp = []
            for line in f:
                if line == '\n':
                    ls.append(tmp)
                    tmp = []
                    continue
                title, val = line[:-1].split(': ')
                x1, y1 = val.split(', ')
                val1 = int(x1[2:])
                val2 = int(y1[2:])
                tmp.append([val1, val2])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def calc(ls, cost, offset=0):
    [x1, y1], [x2, y2], [x_tar, y_tar] = ls
    x_tar += offset
    y_tar += offset
    c1, c2 = cost
    # 104866154726798
    if not y2 * x1 == y1 * x2:
        a = (x_tar * y2 - y_tar * x2) / (x1 * y2 - y1 * x2)
        b = (x_tar - a * x1) / x2
        # only non-negative integer solutions are accepted
        if round(a, 10) == round(a) and round(b, 10) == round(b) and a >= 0 and b >= 0:
            return int(a) * c1 + int(b) * c2
        else:
            return float('inf')
    else:
        res = float('inf')
        if x_tar % x1 == 0 and y_tar % y1 == 0 and x_tar * y1 == y_tar * x1:
            res = min(res, c1 * x_tar // x1)
        if x_tar % x2 == 0 and y_tar % y2 == 0 and x_tar * y2 == y_tar * x2:
            res = min(res, c2 * x_tar // x2)
        return res

if __name__ == "__main__":
    path1 = 'inputFull_20241213.txt'
    # path1 = 'inputPartial_20241213.txt'
    ls = getList(path1)
    # print(ls)
    res1 = 0
    res2 = 0
    for subls in ls:
        tmp_res1 = calc(subls, [3, 1])
        tmp_res2 = calc(subls, [3, 1], 10000000000000)
        # print(tmp_res, subls)
        if tmp_res1 < float('inf'):
            # print(subls)
            res1 += tmp_res1
        if tmp_res2 < float('inf'):
            # print(subls)
            res2 += tmp_res2
    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")