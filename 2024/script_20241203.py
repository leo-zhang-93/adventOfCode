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
                ls.append(line[:-1])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls


def process1(string):
    import re
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, string)
    return matches


def process2(string):
    import re
    pattern = r"don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, string)
    return matches


if __name__ == "__main__":
    path1 = 'inputFull_20241203.txt'
    # path1 = 'inputPartial_20241203.txt'
    ls = getList(path1)

    # Part 1:
    res1 = 0
    for item in ls:
        matches = process1(item)
        matches = [list(map(int, item.replace('mul(', '').replace(')', '').split(','))) for item in matches]
        for item in matches:
            res1 += item[0] * item[1]
    print(res1)

    # Part 2:
    res2 = 0
    # Turns out the do() and don't() does not stop being effective
    # when the line ends. It works on the following line(s)
    # until there's a new "do()" or "don't".
    status = True
    for itm in ls:
        matches = process2(itm)
        len_matches = len(matches)
        for i in range(len_matches):
            item = matches[i]
            if item == 'do()':
                status = True
                continue
            elif item == "don't()":
                status = False
                continue
            if not status:
                continue
            else:
                val1, val2 = list(map(int, item.replace('mul(', '').replace(')', '').split(',')))
                res2 += val1 * val2
    print(res2)
