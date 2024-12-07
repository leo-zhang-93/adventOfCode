def getList(path):
    """Reads and parses the input file, returning sorted lists.

    Args:
        path (str): The path to the input file.

    Returns:
        tuple: A tuple containing two sorted lists of integers.
    """
    ls = []

    try:
        with open(path, 'r') as f:
            for line in f:
                # split the string into results and elements
                item1, item2 = line[:-1].split(': ')
                # further process the results and the elements to int
                res = int(item1)
                ls_elements = list(map(int, item2.split(' ')))
                ls.append([res, ls_elements])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def calc1(target, ls, preval):
    # terminating conditions 1 & 2
    if target < 0:
        return False
    if len(ls) == 0:
        return target == 0
    else:
        # check two scenarios:
        # addition
        # multiplication
        res = False
        res = res or calc1(target - ls[0], ls[1:], ls[0] + preval)
        res = res or calc1(target - preval * (ls[0] - 1), ls[1:], preval * ls[0])
        return res

def calc2(target, ls, preval):
    # import numpy for getting number of digits
    import numpy as np
    if target < 0:
        return False
    if len(ls) == 0:
        return target == 0
    else:
        # check three scenarios:
        # addition
        # concatenation
        # multiplication
        res = False
        res = res or calc2(target - ls[0], ls[1:], ls[0] + preval)
        if ls[0] == 0:
            digits = 1
        else:
            digits = int(np.log10(ls[0])) + 1
        res = res or calc2(target - (preval * (10 ** digits - 1) + ls[0]), ls[1:], preval * (10 ** digits) + ls[0])
        res = res or calc2(target - preval * (ls[0] - 1), ls[1:], preval * ls[0])
        return res

if __name__ == "__main__":
    path1 = 'inputFull_20241207.txt'
    # path1 = 'inputPartial_20241207.txt'
    ls = getList(path1)

    res1 = 0
    res2 = 0
    for i, target, subls in enumerate(ls):
        print(i)
        if calc1(target, subls, 0):
            # print('!')
            res1 += target
        if calc2(target, subls, 0):
            # print('!')
            res2 += target
    print(res1)
    print(res2)