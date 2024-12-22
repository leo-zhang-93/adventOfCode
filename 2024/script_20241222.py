import logging
from typing import Any

logging.basicConfig(level=logging.INFO)

def get_list(path):
    """Reads a file and returns a list of lists of characters."""
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(int(line[:-1]))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []
    return ls

def mix1(sec_num, val):
    return sec_num ^ val

def prune1(sec_num):
    return sec_num % 16777216

def calc1(sec_num):
    sec_num = mix1(sec_num, sec_num * 64)
    sec_num = prune1(sec_num)
    sec_num = mix1(sec_num, int(sec_num / 32))
    sec_num = prune1(sec_num)
    sec_num = mix1(sec_num, sec_num * 2048)
    sec_num = prune1(sec_num)
    return sec_num

def part1(ls):
    res = 0
    for i, val in enumerate(ls):
        if i % 500 == 0:
            logging.info(f"index {i} out of {len(ls)} done!")
        for times in range(2000):
            val = calc1(val)
        res += val
    return res

def part2(ls):
    from collections import defaultdict
    dic = defaultdict(int)
    for i, val in enumerate(ls):
        if i % 500 == 0:
            logging.info(f"index {i} out of {len(ls)} done!")
        tmp_dic = defaultdict(int)
        cnt0 = val % 10
        ls_cnts: list[int] = [cnt0]
        ls_changes = []
        for times in range(2000):
            val = calc1(val)
            cnt = val % 10
            change = cnt - ls_cnts[-1]
            ls_cnts.append(cnt)
            ls_changes.append(change)
            if len(ls_cnts) > 5:
                ls_cnts.pop(0)
                ls_changes.pop(0)
                tp = tuple(ls_changes)
                if tp not in tmp_dic:
                    tmp_dic[tp] = cnt
        for key in tmp_dic:
            dic[key] += tmp_dic[key]

    return max(dic.values())

if __name__ == "__main__":
    path1 = 'inputFull_20241222.txt'
    # path1 = 'inputPartial_20241222.txt'
    input_ls = get_list(path1)
    print(f"Part 1: {part1(input_ls)}")
    print()
    print(f"Part 2: {part2(input_ls)}")
