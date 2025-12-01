def dial(path):
    ls_actions = []
    try:
        with open(path, 'r') as f:
            for line in f:
                action = line[:-1]
                direction = action[0]
                steps = int(action[1:])
                ls_actions.append((direction, steps))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []
    return ls_actions

def calc1(path, start, num):
    ls_actions = dial(path)
    pos = start
    res = 0
    for direction, steps in ls_actions:
        if direction == 'R':
            pos += steps
        else:
            pos -= steps
        pos %= num
        if not pos:
            res += 1
    return res

def calc2(path, start, num):
    ls_actions = dial(path)
    pos = start
    res = 0
    for direction, steps in ls_actions:
        if direction == 'R':
            newpos = pos + steps
        else:
            newpos = pos - steps
        if newpos >= num:
            res += newpos // num
        if pos > 0:
            if newpos <= 0:
                res += abs((newpos - 1)// num)
        else:
            if newpos <= 0:
                res += abs((newpos - 1)// num) - 1
        pos = newpos % num
    return res

if __name__ == "__main__":
    path1 = 'input20251201_Sample.txt'
    path2 = 'input20251201_Partial.txt'
    # Part 1:
    print(f"Part 1: {calc1(path2, 50, 100)}")
    # Part 2:
    print(f"Part 2: {calc2(path2, 50, 100)}")
