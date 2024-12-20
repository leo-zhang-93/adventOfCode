def getList(path):
    ls1 = []
    ls2 = []
    try:
        with open(path, 'r') as f:
            for line in f:
                val1, val2 = map(int, line[:-1].split('   '))
                ls1.append(val1)
                ls2.append(val2)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return [], []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []

    return ls1, ls2


def calc1(path):
    ls1, ls2 = getList(path)
    ls1 = sorted(ls1)
    ls2 = sorted(ls2)
    n = len(ls1)
    return sum([abs(ls1[i] - ls2[i]) for i in range(n)])


def calc2(path):
    from collections import Counter
    ls1, ls2 = getList(path)
    res = 0
    counter1 = Counter(ls1)
    counter2 = Counter(ls2)
    for key in counter1.keys():
        res += key * counter1[key] * counter2[key]
    return res


if __name__ == "__main__":
    # path1 = 'inputPartial_20241201.txt'
    path1 = 'inputFull_20241201.txt'
    # Part 1:
    print(f"Part 1: {calc1(path1)}")
    # Part 2:
    print(f"Part 2: {calc2(path1)}")
