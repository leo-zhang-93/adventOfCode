def getList(path):
    ls = []
    ls_instructions = []
    try:
        with open(path, 'r') as f:
            for line in f:
                if 'Register' in line:
                    ls.append(int(line[:-1].split(": ")[1]))
                elif line == '\n':
                    continue
                else:
                    res = line[:-1].split(' ')[1]
                    ls_instructions = list(map(int, res.split(',')))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return [], []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []

    return ls, ls_instructions


def call(idx):
    return ls[idx]

def func0(operand):
    res = ls[0] / 2 ** combo(operand)
    ls[0] = int(res)
    ls_point[0] += 2

def func1(operand):
    ls[1] = ls[1] ^ operand
    ls_point[0] += 2

def func2(operand):
    ls[1] = combo(operand) % 8
    ls_point[0] += 2

def func3(operand):
    if ls[0] == 0:
        ls_point[0] += 2
        return
    ls_point[0] = operand

def func4(operand):
    ls[1] = ls[1] ^ ls[2]
    ls_point[0] += 2

def func5(operand):
    ls_point[0] += 2
    return combo(operand) % 8

def func6(operand):
    res = ls[0] / 2 ** combo(operand)
    ls[1] = int(res)
    ls_point[0] += 2

def func7(operand):
    res = ls[0] / 2 ** combo(operand)
    ls[2] = int(res)
    ls_point[0] += 2

def combo(operand):
    if operand <= 3:
        return operand
    return call(operand - 4)

ls_funcs = [
    func0,
    func1,
    func2,
    func3,
    func4,
    func5,
    func6,
    func7,
]


if __name__ == "__main__":
    path1 = 'inputFull_20241217.txt'
    # path1 = 'inputPartial_20241217.txt'
    ls, ls_instructions = getList(path1)
    target = ','.join(map(str, ls_instructions))
    print(ls, ls_instructions)
    ls_point = [0]
    res = []
    while True:
        if ls_point[0] >= len(ls_instructions) - 1:
            break
        idx = ls_point[0]
        if idx == 0:
            val = ls[0]
        opcode = ls_instructions[idx]
        operand = ls_instructions[idx + 1]
        tmp_res = ls_funcs[opcode](operand)
        if tmp_res is not None:
            res.append(tmp_res)
    result = ','.join(map(str, res))
    print(f"Part 1: {result}")

    # output = ((val % 8) ^ 1 ^ 5) ^ (int(val / 2 ** (val % 8 ^ 1))) % 8:
    # val = val // 8
    init = 0
    queue = [0]
    tmp = []
    for i, digit in enumerate(ls_instructions[::-1]):
        while queue:
            init = queue.pop(0)
            for add_val in range(8):
                val = init + add_val
                if digit == ((val % 8) ^ 1 ^ 5) ^ (int(val / 2 ** (val % 8 ^ 1))) % 8:
                    tmp.append(val * 8)
            if not queue:
                if i == len(ls_instructions) - 1:
                    print(f"Part 2: {tmp[0] // 8}")
                queue = tmp
                tmp = []
                break







