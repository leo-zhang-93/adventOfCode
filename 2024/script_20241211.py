# Travel@Phuket 2024.12.11 Happy Birthday!
# Before boarding the boat from Phuket to Phi Phi
def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls = list(map(int, line[:-1].split(' ')))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def part(ls, times):
    dic = {}

    def calc(val, times):
        if (val, times) in dic:
            return dic[(val, times)]
        if times == 0:
            return 1
        else:
            if val == 0:
                res = calc(1, times - 1)
            elif len(str(val)) % 2 == 0:
                nlen = len(str(val))
                res = calc(int(str(val)[:nlen // 2]), times - 1)
                res += calc(int(str(val)[nlen // 2:]), times - 1)
            else:
                res = calc(val * 2024, times - 1)
            dic[(val, times)] = res
            return res

    res = 0
    for val in ls:
        res += calc(val, times)
    return res

if __name__ == "__main__":
    path1 = 'inputFull_20241211.txt'
    ls = getList(path1)
    # Part 1:
    print(f"Part 1: {part(ls, 25)}")
    # Part 2:
    print(f"Part 2: {part(ls, 75)}")
