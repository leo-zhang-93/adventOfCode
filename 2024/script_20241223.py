def get_list(path):
    """Reads a file and returns a list of lists of characters."""
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(line[:-1].split('-'))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []
    return ls

def calc1(ls):
    from collections import defaultdict
    dic = defaultdict(list)
    for u, v in ls:
        dic[u].append(v)
        dic[v].append(u)
    res = 0
    seen = set([])
    for key in dic.keys():
        length = len(dic[key])
        for i in range(length - 1):
            node1 = dic[key][i]
            for j in range(i + 1, length):
                node2 = dic[key][j]
                tp = tuple(sorted([key, node1, node2]))
                if node1 in dic[node2] and tp not in seen:
                    seen.add(tp)
                    flag = 0
                    for val in tp:
                        if val.startswith('t'):
                            flag = 1
                            break
                    if flag == 1:
                        res += 1
    return res


def calc2(ls):
    from collections import defaultdict
    dic = defaultdict(set)
    for u, v in ls:
        dic[u].add(v)
        dic[v].add(u)

    result = 0
    dic_combo = {}
    def combos(tp):
        if tp in dic_combo:
            return dic_combo[tp]
        if len(tp) == 1:
            val = tp[0]
            dic_combo[tp] = [[val], []]
            return [[val], []]
        else:
            res = []
            sub_res = combos(tp[1:])
            res += [[tp[0]] + item for item in sub_res]
            res += [item for item in sub_res]
            dic_combo[tp] = res
            return res

    def check(ls):
        flag = 0
        st = set(ls)
        for val in ls:
            if val in dic:
                if len(st.intersection(dic[val])) != len(st) - 1:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if flag == 1:
            return False
        return True

    result_dic = {}
    for key in dic.keys():
        tp = tuple(sorted(dic[key].union({key})))
        combo = sorted(combos(tp), key=lambda x: -len(x))
        for item in combo:
            if check(item):
                result = max(result, len(item))
                result_dic[len(item)] = item
                break
    print(result)
    return ','.join(result_dic[result])

if __name__ == "__main__":
    path1 = 'inputFull_20241223.txt'
    # path1 = 'inputPartial_20241223.txt'
    input_ls = get_list(path1)
    # print(input_ls)
    print(f"Part 1: {calc1(input_ls)}")
    print(f"Part 2: {calc2(input_ls)}")