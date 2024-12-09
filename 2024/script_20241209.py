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


"""
The problem is not stated clearly and there lacks enough examples.
The examples only give cases where ID <= 9.
What about more files and ID > 9, i.e. with more than one digit? 
For example, if we have a file of 4 blocks with ID = 10, should it be [1, 0, 1, 0, 1, 0, 1, 0], 
or [0, 0, 0, 0] (because the problem mentions "one digit", which could be the last, or 
[10, 10, 10, 10]. The third turned out to be correct. 
The designer could slightly tweak the examples to cover the case that ID has more than one digit. 
It would be clearer! 
"""


def calc1(ls):
    n = len(ls)
    # here newls keeps the actual list
    # e.g. A 5-block with ID = 12 would be represented as [..., 12, 12, 12, 12, 12, ...] in newls.
    # All elements of newls are either ID value in integer or '.'.
    newls = []
    idx = 0
    for i in range(n):
        val = int(ls[i])
        if i % 2 == 0:
            newls += [idx] * val
            idx += 1
        else:
            newls += ['.'] * val
    left = 0
    right = len(newls) - 1
    while left < right:
        while newls[left] != '.':
            left += 1
        while newls[right] == '.':
            right -= 1
        newls[left], newls[right] = newls[right], newls[left]
        left += 1
        right -= 1
    res = 0
    for i in range(right + 1):
        if newls[i] == '.':
            break
        res += i * newls[i]
    return res


def calc2(ls):
    n = len(ls)
    # here newls keeps the lists of [ID (or space), number of blocks, start index]
    # this would be easier to handle as we need to move the file blocks together.
    # e.g. A 5-block with ID = 12, starting at index 90 would be represented as [...,[12, 5, 90], ...] in newls.
    # All elements of newls are list of three elements, which represent ID, number of blocks, and the start index.
    newls = []
    idx = 0
    start_idx = 0
    for i in range(n):
        val = int(ls[i])
        if i % 2 == 0:
            newls.append([idx, val, start_idx])
            idx += 1
            start_idx += val
        else:
            if val > 0:
                newls.append(['.', val, start_idx])
                start_idx += val

    res = 0
    curr_idx = newls[-1][0]
    """
    newls is handled from index -1 to index 0.
    If the last block is spaces, pop and continue.
    If the last block is file, from index 0 to -1, find a block of spaces can hold: 
        If there's such block, put the file in, update the space block, and calculate the checksum. 
        if no such block, calculate the checksum at the original location
        Anyways, this file is no longer needed and can be popped. 
    """

    while newls:
        idx, val, start_idx = newls[-1]
        if idx == '.':
            newls.pop()
            continue
        flag = 0
        for i in range(len(newls)):
            if newls[i][0] == '.' and newls[i][1] >= val:
                flag = 1
                newls.pop()
                for ii in range(val):
                    res += idx * (newls[i][2] + ii)
                if newls[i][1] > val:
                    newls[i][1] -= val
                    newls[i][2] += val
                else:
                    newls.pop(i)
                break
        if flag == 0:
            for ii in range(val):
                res += idx * (start_idx + ii)
            newls.pop()
    return res


if __name__ == "__main__":
    path1 = 'inputFull_20241209.txt'
    # path1 = 'inputPartial_20241209.txt'
    ls = getList(path1)[0]

    # Part 1:
    print(calc1(ls))

    # Part 2:
    print(calc2(ls))
