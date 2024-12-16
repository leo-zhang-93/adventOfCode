# On the taxi to Phuket Airport
# Part 2 is a difficult problem!
def getList(path):
    ls_grid = []
    ls_movements = []
    try:
        with open(path, 'r') as f:
            flag = 0
            for i, line in enumerate(f):
                if i == 0:
                    continue
                if '#######' in line:
                    continue
                if line == '\n':
                    flag = 1
                    continue
                if flag == 0:
                    ls_grid.append(list(line[1:-2]))
                else:
                    ls_movements += list(line[:-1])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls_grid, ls_movements

def check1(ls_grid, ls_movements):
    m, n = len(ls_grid), len(ls_grid[0])
    for i in range(m):
        flag = 0
        for j in range(n):
            if ls_grid[i][j] == '@':
                flag = 1
                break
        if flag == 1:
            break
    x = i
    y = j
    directions = {
        '^': [-1, 0],
        '<': [0, -1],
        '>': [0, 1],
        'v': [1, 0],
    }

    for drct in ls_movements:
        dx, dy = directions[drct]
        xx = x + dx
        yy = y + dy
        xx0 = xx
        yy0 = yy
        if 0 <= xx < m and 0 <= yy < n:
            if ls_grid[xx][yy] in '@.':
                x = xx
                y = yy
            elif ls_grid[xx][yy] == '#':
                continue
            else:
                flag = 0
                while 0 <= xx < m and 0 <= yy < n:
                    if ls_grid[xx][yy] in '@.':
                        ls_grid[xx][yy], ls_grid[xx0][yy0] = ls_grid[xx0][yy0], ls_grid[xx][yy]
                        x = xx0
                        y = yy0
                        break
                    elif ls_grid[xx][yy] == '#':
                        break
                    xx += dx
                    yy += dy
    res = 0
    for i in range(m):
        for j in range(n):
            if ls_grid[i][j] == 'O':
                res += (i + 1) * 100 + j + 1
    return res

def check2(ls_grid, ls_movements):
    m, n = len(ls_grid), len(ls_grid[0])
    # create a new table to store the expanded table
    newls_grid = []
    for i in range(m):
        for j in range(n):
            if j == 0:
                newls_grid.append([])
            val = ls_grid[i][j]
            if val == 'O':
                newls_grid[-1].append('[')
                newls_grid[-1].append(']')
            elif val == '#':
                newls_grid[-1].append('#')
                newls_grid[-1].append('#')
            elif val == '.':
                newls_grid[-1].append('.')
                newls_grid[-1].append('.')
            elif val == '@':
                newls_grid[-1].append('@')
                newls_grid[-1].append('.')
    newm, newn = len(newls_grid), len(newls_grid[0])

    # find the start coordinate
    for i in range(newm):
        flag = 0
        for j in range(newn):
            if newls_grid[i][j] == '@':
                flag = 1
                break
        if flag == 1:
            break
    x = i
    y = j

    # set up the dict between signs and x, y changes
    directions = {
        '^': [-1, 0],
        '<': [0, -1],
        '>': [0, 1],
        'v': [1, 0],
    }

    def allBlocksHorizontal(x, y, dx, dy):
        # Horizontal movement is easier
        # because the blocks are always 1 cell tall
        # horizontal movement only involve the blocks in the row
        st = set()
        queue = [[x, y]]
        flag = 0
        while queue:
            x_, y_ = queue.pop(0)
            xx = x_ + dx
            yy = y_ + dy
            if 0 <= xx < newm and 0 <= yy < newn:
                if newls_grid[xx][yy] == '#':
                    flag = 1
                    break
                elif newls_grid[xx][yy] in '[]':
                    queue.append([xx, yy])
                    st.add((xx, yy))
                else:
                    break
            else:
                flag = 1
                break
        if flag == 0:
            return sorted(st, key=lambda x: [-dy * x[1]])
        return []

    def allBlocksVertical(x, y, dx, dy):
        # this is harder as the example illustrate
        # need to use leveled queue to determine whether all can be moved
        st = set()
        queue = [[x, y]]
        tmp = []
        flag = 0
        while queue:
            x_, y_ = queue.pop(0)
            xx = x_ + dx
            yy = y_ + dy
            if 0 <= xx < newm and 0 <= yy < newn: # new cells in the grid (not hitting the border wall)
                if newls_grid[xx][yy] == '[':
                    if (xx, yy) not in st:
                        st.add((xx, yy))
                        tmp.append([xx, yy])
                    if (xx, yy + 1) not in st:
                        st.add((xx, yy + 1))
                        tmp.append((xx, yy + 1))
                elif newls_grid[xx][yy] == ']':
                    if (xx, yy) not in st:
                        st.add((xx, yy))
                        tmp.append([xx, yy])
                    if (xx, yy - 1) not in st:
                        st.add((xx, yy - 1))
                        tmp.append((xx, yy - 1))
                elif newls_grid[xx][yy] == '#':
                    # vetoed by hitting a wall
                    flag = 1
                    break
            else:
                # vetoed by hitting a border wall
                flag = 1
                break
            if not queue:
                queue = tmp
                tmp = []
        if flag == 1:
            return []
        else:
            return sorted(st, key=lambda var: [-dx * var[0], var[1]])

    def changeVar(ls, dx, dy):
        # to switch the values
        for x, y in ls:
            newls_grid[x + dx][y + dy], newls_grid[x][y] = newls_grid[x][y], newls_grid[x + dx][y + dy]

    for drct in ls_movements:
        dx, dy = directions[drct]
        xx = x + dx
        yy = y + dy
        xx0 = xx
        yy0 = yy
        if 0 <= xx < newm and 0 <= yy < newn:
            if newls_grid[xx][yy] in '@.':
                x = xx
                y = yy
            elif newls_grid[xx][yy] == '#':
                continue
            else:
                if dy != 0:
                    # if move horizontally, use the horizontal function
                    ls_blocks = allBlocksHorizontal(x, y, dx, dy)
                    if ls_blocks:
                        changeVar(ls_blocks, dx, dy)
                        x = xx
                        y = yy
                else: # dx == 0
                    # use the vertical function if moving vertically
                    ls_blocks = allBlocksVertical(x, y, dx, dy)
                    if ls_blocks:
                        changeVar(ls_blocks, dx, dy)
                        x = xx
                        y = yy
    res = 0

    for i in range(newm):
        for j in range(newn):
            if newls_grid[i][j] in '[':
                # need to have j + "2" because the order wall duplicated
                res += (i + 1) * 100 + j + 2
    return res

if __name__ == "__main__":
    path1 = 'inputFull_20241215.txt'
    # path1 = 'inputPartial_20241215.txt'
    # path1 = 'inputPartial01_20241215.txt'
    ls_grid, ls_movements = getList(path1)
    print(f"Part 1: {check1(ls_grid, ls_movements)}")

    # need to reload the lists as part 1 has modified them
    ls_grid, ls_movements = getList(path1)
    print(f"Part 2: {check2(ls_grid, ls_movements)}")



