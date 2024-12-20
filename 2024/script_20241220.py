# The problem today is quite troublesome
# because I did not manage to jump out of the mindset I used for part 1
# I was purely trying to replicate what I did for part 1 for part 2 but failed.
# then I looked at the input file and noticed the path is actually taking up all blank cells and there's a cloud
# between S and E.
# Seeing the grid reminded me of the snakes and the ladders.
# Do I really need to use bfs to know the distance? Can I just loop and for each blank I found blanks with 20 steps away
# if the new path can save me 100+ picoseconds then count it.. Time complexity would be O(10**6) - handlable.
# Then Bang! It's resolve (~7 hours after release...)

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


def calc(ls, offset, radius):

    from collections import defaultdict

    m, n = len(ls), len(ls[0])

    startx = None
    starty = None
    endx = None
    endy = None
    ls_ponds = []
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 'S':
                startx = i
                starty = j
            if ls[i][j] == 'E':
                endx = i
                endy = j
            if ls[i][j] == '#':
                ls_ponds.append([i, j])

    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    queue = [[startx, starty]]
    seen = set([(startx, starty)])
    tmp = []
    level = 1
    flag = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen and ls[xx][yy] != '#':
                tmp.append([xx, yy])
                seen.add((xx, yy))
                if xx == endx and yy == endy:
                    bench = level
                    flag = 1
                    break
        if flag == 1:
            break
        if not queue:
            queue = tmp
            tmp = []
            level += 1

    dic_from_s = defaultdict(lambda: float('inf'))
    dic_from_s[(startx, starty)] = 0
    queue = [[startx, starty]]
    tmp = []
    level = 1
    seen = set([(startx, starty)])
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen and ls[xx][yy] != '#':
                dic_from_s[(xx, yy)] = level
                tmp.append([xx, yy])
                seen.add((xx, yy))
        if not queue:
            queue = tmp
            tmp = []
            level += 1

    dic_from_e = defaultdict(lambda: float('inf'))
    dic_from_e[(endx, endy)] = 0
    queue = [[endx, endy]]
    tmp = []
    level = 1
    seen = set([(endx, endy)])
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen and ls[xx][yy] != '#':
                dic_from_e[(xx, yy)] = level
                tmp.append([xx, yy])
                seen.add((xx, yy))
        if not queue:
            queue = tmp
            tmp = []
            level += 1

    res = 0
    for i in range(m):
        for j in range(n):
            if ls[i][j] != '#':
                for di in range(-radius, radius + 1):
                    for dj in range(-(radius - abs(di)), radius - abs(di) + 1):
                        if di == 0 and dj == 0:
                            continue
                        newi = i + di
                        newj = j + dj
                        if (0 <= newi < m and 0 <= newj < n and ls[newi][newj] != '#'
                                and dic_from_s[(i, j)] + dic_from_e[(newi, newj)] + abs(di) + abs(
                                    dj) + offset <= bench):
                            res += 1
    return res

if __name__ == "__main__":
    path1 = 'inputFull_20241220.txt'
    # path1 = 'inputPartial_20241220.txt'
    ls = getList(path1)
    print(f"Part 1: {calc(ls, 100, 2)}")
    print(f"Part 2: {calc(ls, 100, 20)}")












