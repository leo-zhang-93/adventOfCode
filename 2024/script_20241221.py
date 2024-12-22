def get_list(path):
    """Reads a file and returns a list of lists of characters."""
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                ls.append(list(line.strip()))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []
    return ls

# Numeric pad configuration
grid1 = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A']
]

# Position of each number on the numeric pad
dic_pos1 = {
    '0': [3, 1],
    '1': [2, 0],
    '2': [2, 1],
    '3': [2, 2],
    '4': [1, 0],
    '5': [1, 1],
    '6': [1, 2],
    '7': [0, 0],
    '8': [0, 1],
    '9': [0, 2],
    'A': [3, 2],
}

# Directions for movement
directions = [
    [0, 1, '>'],
    [0, -1, '<'],
    [1, 0, 'v'],
    [-1, 0, '^'],
]

# Store paths for numeric pad
dic_paths1 = {}

# Calculate the path from s to e on the numeric pad
def calc_dist_num(s, e):
    """Calculates the path from s to e on the numeric pad."""
    if s == e:
        return ['']
    if (s, e) in dic_paths1:
        return dic_paths1[(s, e)]
    sx, sy = dic_pos1[s]
    ex, ey = dic_pos1[e]
    res = []
    for dx, dy, sign in directions:
        xx = sx + dx
        yy = sy + dy
        if (0 <= xx < len(grid1) and 0 <= yy < len(grid1[0]) and grid1[xx][yy] != '#' and
                min(sx, ex) <= xx <= max(sx, ex) and min(sy, ey) <= yy <= max(sy, ey)):
            res += [sign + item for item in calc_dist_num(grid1[xx][yy], e)]
    dic_paths1[(s, e)] = res
    return res

# Directional pad configuration
grid2 = [
    ['#', '^', 'A'],
    ['<', 'v', '>'],
]

# Position of each number on the directional pad
dic_pos2 = {
    '^': [0, 1],
    'A': [0, 2],
    '<': [1, 0],
    'v': [1, 1],
    '>': [1, 2],
}

# Store paths for directional pad
dic_paths2 = {}

# Calculate the path from s to e on the directional pad
def calc_dist_dir(s, e):
    """Calculates the path from s to e on the directional pad."""
    if s == e:
        return ['']
    if (s, e) in dic_paths2:
        return dic_paths2[(s, e)]
    sx, sy = dic_pos2[s]
    ex, ey = dic_pos2[e]
    res = []
    for dx, dy, sign in directions:
        xx = sx + dx
        yy = sy + dy
        if (0 <= xx < len(grid2) and 0 <= yy < len(grid2[0]) and grid2[xx][yy] != '#' and
                min(sx, ex) <= xx <= max(sx, ex) and min(sy, ey) <= yy <= max(sy, ey)):
            res += [sign + item for item in calc_dist_dir(grid2[xx][yy], e)]
    dic_paths2[(s, e)] = res
    return res

# Part 1
def part1(ls):
    """Calculates the result for part 1.
    This function was based on my initial understanding of the problem.
    The idea was intuitive but quite complex to implement and also slow for more layers of robots (part 2).
    """
    # initialize the complexities.
    result = 0
    for doorcode in ls:
        doorcode = ['A'] + doorcode
        tmp_ls = []
        length = len(doorcode)
        for i in range(1, length):
            tmp_paths = calc_dist_num(doorcode[i - 1], doorcode[i])
            if not tmp_ls:
                tmp_ls = [[item] for item in tmp_paths]
            else:
                tmp_ls = [item1 + [item2] for item1 in tmp_ls for item2 in tmp_paths]
        # newls contains the new instructions needed for hitting the door codes on the numeric pad.
        newls = ['A' + 'A'.join(item) + 'A' for item in tmp_ls]

        newls1 = []
        for string1 in newls:
            length1 = len(string1)
            tmp_ls1 = []
            for i in range(1, length1):
                tmp_paths = calc_dist_dir(string1[i - 1], string1[i])
                if not tmp_ls1:
                    tmp_ls1 = [[item] for item in tmp_paths]
                else:
                    tmp_ls1 = [item1 + [item2] for item1 in tmp_ls1 for item2 in tmp_paths]
            # newls1 contains the new instructions needed for hitting the newls code on the directional pad.
            newls1 += ['A' + 'A'.join(item) + 'A' for item in tmp_ls1]

        res = float('inf')
        for string2 in newls1:
            total = 0
            length2 = len(string2)
            for i in range(1, length2):
                tmp_length = len(calc_dist_dir(string2[i - 1], string2[i])[0])
                tmp_length += 1
                total += tmp_length
            res = min(res, total)
        val = int(''.join(doorcode[1:-1]))
        # add up the complexities.
        result += val * res

    return result

# Part 2 will use another way to tackle the problem from part 1.
# Instead of explicitly constructing the result string, we count the length instead.

# mapping between combos of two consecutive instructions and the possible new combos it brings up.
dic_paths2_explicit = {
    '^A': [['A>', '>A']],
    '^<': [['Av', 'v<', '<A']],
    '^v': [['Av', 'vA']],
    '^>': [['Av', 'v>', '>A'], ['A>', '>v', 'vA']],
    'A^': [['A<', '<A']],
    'A<': [['Av', 'v<', '<<', '<A'], ['A<', '<v', 'v<', '<A']],
    'Av': [['A<', '<v', 'vA'], ['Av', 'v<', '<A']],
    'A>': [['Av', 'vA']],
    '<^': [['A>', '>^', '^A']],
    '<A': [['A>', '>>', '>^', '^A'], ['A>', '>^', '^>', '>A']],
    '<v': [['A>', '>A']],
    '<>': [['A>', '>>', '>A']],
    'v^': [['A^', '^A']],
    'vA': [['A>', '>^', '^A'], ['A^', '^>', '>A']],
    'v<': [['A<', '<A']],
    'v>': [['A>', '>A']],
    '>^': [['A<', '<^', '^A'], ['A^', '^<', '<A']],
    '>A': [['A^', '^A']],
    '><': [['A<', '<<', '<A']],
    '>v': [['A<', '<A']]
}

# store the results for each calculation to avoid recalculating.
dic_keep = {}
# Calculate the length of result string generated from s and e after certain times.
def calculate(s, e, times):
    if (s, e, times) in dic_keep:
        return dic_keep[(s, e, times)]
    if times == 0:
        return 2
    if times == 1:
        return len(dic_paths2_explicit.get(s + e, [['AA']])[0])
    else:
        res = float('inf')
        for subs in dic_paths2_explicit.get(s + e, [['AA']]):
            tmp_res = 0
            for news, newy in subs:
                tmp_res += calculate(news, newy, times - 1)
            res = min(res, tmp_res)
        dic_keep[(s, e, times)] = res
        return res

def part2(ls):
    """Calculates the result for part 2.
    The first half is the same while the second half changes to the new way.
    """
    result = 0
    for doorcode in ls:
        # first half
        doorcode = ['A'] + doorcode
        tmp_ls = []
        length = len(doorcode)
        for i in range(1, length):
            tmp_paths = calc_dist_num(doorcode[i - 1], doorcode[i])
            if not tmp_ls:
                tmp_ls = [[item] for item in tmp_paths]
            else:
                tmp_ls = [item1 + [item2] for item1 in tmp_ls for item2 in tmp_paths]
        newls = ['A' + 'A'.join(item) + 'A' for item in tmp_ls]

        # second half
        min_count = float('inf')
        for subs in newls:
            tmp_res = 0
            n = len(subs)
            for i in range(1, n):
                tmp_res += calculate(subs[i - 1], subs[i], 25)
            min_count = min(min_count, tmp_res)
        result += int(''.join(doorcode[1:-1])) * min_count
    return result

if __name__ == "__main__":
    path1 = 'inputFull_20241221.txt'
    input_ls = get_list(path1)
    print(f'Part 1: {part1(input_ls)}')
    print(f'Part 2: {part2(input_ls)}')












