def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                # convert it to list of lists for value overrides.
                ls.append(list(line[:-1]))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls

def check1(ls):
    m = len(ls)
    n = len(ls[0])
    print(m, n)
    dic_dirs = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0)
    }
    dx, dy = [-1, 0]
    flag = 0
    for i in range(m):
        for j in range(n):
            if ls[i][j] == '^':
                flag = 1
                break
        if flag == 1:
            break
    seen = set([(i, j)])
    while 0 <= i < m and 0 <= j < n: 
        ii = i + dx
        jj = j + dy
        if not (0 <= ii < m and 0 <= jj < n): 
            break
        if ls[ii][jj] in '.^':
            i = ii
            j = jj
            seen.add((i, j))
        else:
            dx, dy = dic_dirs[(dx, dy)]
        # print(i, j)
    print(seen)
    return len(seen)

def check2(ls):
    # TBH, I don't have much better solution than this traverse..
    # this is a bit slow, taking several minutes to run, but effective.
    # in general to find whether a combination of cell + the direction has been seen before.
    # if so, there's definitely a loop. Otherwise, the guard will go out of the map.
    m = len(ls)
    n = len(ls[0])
    dic_dirs = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0)
    }

    ls_blanks = []
    start = []
    for i in range(m):
        for j in range(n):
            if ls[i][j] == '^':
                start = [i, j]
            elif ls[i][j] == '.':
                ls_blanks.append([i, j])

    res = 0
    for i_blank, j_blank in ls_blanks:
        ls[i_blank][j_blank] = '#'
        dx, dy = [-1, 0]
        i, j = start
        seen = set([(i, j, dx, dy)])
        while 0 <= i < m and 0 <= j < n:
            ii = i + dx
            jj = j + dy
            if not (0 <= ii < m and 0 <= jj < n):
                break
            elif ls[ii][jj] == '#':
                dx, dy = dic_dirs[(dx, dy)]
                seen.add((i, j, dx, dy))
            elif ls[ii][jj] in '.^':
                if (ii, jj, dx, dy) in seen:
                    res += 1
                    break
                i = ii
                j = jj
                seen.add((i, j, dx, dy))
        ls[i_blank][j_blank] = '.'
    return res


if __name__ == "__main__":
    path1 = 'inputFull_20241206.txt'
    # path1 = 'inputPartial_20241206.txt'
    ls = getList(path1)
    # Part 1:
    print(check1(ls))
    # Part 2:
    print(check2(ls))