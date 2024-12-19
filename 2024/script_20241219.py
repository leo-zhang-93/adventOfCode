def getList(path):
    ls1 = []
    ls2 = []
    flag = 0
    try:
        with open(path, 'r') as f:
            for line in f:
                if line == '\n':
                    flag = 1
                    continue
                if flag == 0:
                    ls1.append(line[:-1].split(', '))
                else:
                    ls2.append(line[:-1])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return [], []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []

    return ls1, ls2


def calc1(string):
    if string in dic_string1:
        return dic_string1[string]
    if string in set_ls1:
        dic_string1[string] = True
        return True
    else:
        res = False
        for substring in set_ls1:
            if string.startswith(substring):
                res = res or calc1(string[len(substring):])
                if res:
                    dic_string1[string] = True
                    return True
        dic_string1[string] = False
        return False


def calc2(string):
    if string in dic_string2:
        return dic_string2[string]
    res = 0
    for substring in set_ls1:
        if substring == string:
            res += 1
        if string.startswith(substring):
            res += calc2(string[len(substring):])
    dic_string2[string] = res
    return res


if __name__ == "__main__":
    path1 = 'inputFull_20241219.txt'
    # path1 = 'inputPartial_20241219.txt'
    ls1, ls2 = getList(path1)
    set_ls1 = set(ls1[0])
    dic_string1 = {}
    dic_string2 = {}
    result1 = 0
    result2 = 0
    for string in ls2:
        if calc1(string):
            result1 += 1
        result2 += calc2(string)
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
