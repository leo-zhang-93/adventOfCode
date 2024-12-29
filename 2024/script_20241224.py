def get_list(path):
    """Reads a file and returns a list of lists of characters."""
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
                    tmp = line[:-1].split(': ')
                    tmp[1] = int(tmp[1])
                    ls1.append(tmp)
                else:
                    tmp = line[:-1].split(' ')
                    ls2.append(tmp[:3] + tmp[4:])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return [], []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []
    return ls1, ls2

def funcAND(x, y):
    return x & y

def funcOR(x, y):
    return x | y

def funcXOR(x, y):
    return x ^ y

if __name__ == "__main__":
    path1 = 'inputFull_20241224.txt'
    # path1 = 'inputPartial_20241224.txt'
    input_ls1, input_ls2 = get_list(path1)
    dic_funcs = {
        'AND': funcAND,
        'OR': funcOR,
        'XOR': funcXOR
    }
    dic = {}
    dic_parents = {}
    for key, val in input_ls1:
        dic[key] = val
    tmp = []
    while input_ls2:
        x, func, y, assign = input_ls2.pop(0)
        if (x not in dic) or (y not in dic):
            tmp.append([x, func, y, assign])
        else:
            dic[assign] = dic_funcs[func](dic[x], dic[y])
            dic_parents[assign] = [x, y]
        if not input_ls2:
            input_ls2 = tmp
            tmp = []

    keys_z = sorted([key for key in dic.keys() if key.startswith('z')], reverse=True)
    for keyz in keys_z:
        tmp_res = [keyz]
        result = [keyz]
        while tmp_res:
            key = tmp_res.pop(0)
            if key in dic_parents:
                for newkey in dic_parents[key]:
                    if newkey not in result:
                        result.append(newkey)
                        tmp_res.append(newkey)
    # keys_x = sorted([key for key in dic.keys() if key.startswith('x')], reverse=True)
    # keys_y = sorted([key for key in dic.keys() if key.startswith('y')], reverse=True)
    print('Part 1:', int(''.join([str(dic[item]) for item in keys_z]), 2))
    # I can only solve the part two by looking into
    # 1) the difference between binary value of z keys and sum of x and y keys
    # 2) imply the trouble some values of z*
    # 3) find the patterns of the binary adding and locate the wrong values
    print('Part 2:', ','.join(sorted(['nnt','gws','z13','npf','z19','cph','hgj','z33'])))