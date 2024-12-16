# Typical Dijkstra Algo!
# Just need to mind that the directions need to be kept as well
def getList(path):
    ls = []
    try:
        with open(path, 'r') as f:
            for line in f:
                # if line == '#' * (len(line) - 1) + '\n':
                #     continue
                # else:
                ls.append(line[0:-1])
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return []

    return ls


def check(ls):
    from collections import defaultdict
    import heapq
    m, n = len(ls), len(ls[0])
    startx, starty = m - 2, 1
    endx, endy = 1, n - 2
    dic_dis = defaultdict(lambda: float('inf'))
    dic_dis[(startx, starty, 0, 1)] = 0
    # distance, [x, y, (dx, dy)]
    # only distance is used for sorting the second element is for reference data
    # the dx, dy is also necessary because the costs to enter a cell in different directions are different
    queue = [(0, [startx, starty, (0, 1)])]
    heapq.heapify(queue)
    dic_directions = {
        (0, 1): [(1, 0), (-1, 0), (0, -1)],
        (0, -1): [(1, 0), (-1, 0), (0, 1)],
        (1, 0): [(0, 1), (0, -1), (-1, 0)],
        (-1, 0): [(0, 1), (0, -1), (1, 0)],
    }

    # the dictionary to keep the links between cells * direction and its parents cell * direction.
    # direction is necessary here too
    dic_link = defaultdict(set)
    # to keep the ending status
    keep = []
    while queue:
        # print(queue)
        dis, [x, y, (dx, dy)] = heapq.heappop(queue)
        if x == endx and y == endy:
            # when we first see the end cell, it's the solution and we can stop here
            keep = [x, y, dx, dy]
            res_dis = dis
            break
        xx = x + dx
        yy = y + dy
        if 0 <= xx < m and 0 <= yy < n and ls[xx][yy] != '#' and dis + 1 <= dic_dis[(xx, yy, dx, dy)]:
            if dis + 1 < dic_dis[(xx, yy, dx, dy)]:
                dic_link[(xx, yy, dx, dy)] = {(x, y, dx, dy)}
            else:
                dic_link[(xx, yy, dx, dy)].add((x, y, dx, dy))
            dic_dis[(xx, yy, dx, dy)] = 1 + dis
            heapq.heappush(queue, (1 + dis, [xx, yy, (dx, dy)]))
        for i, (dx_, dy_) in enumerate(dic_directions[(dx, dy)]):
            xx = x + dx_
            yy = y + dy_
            if (0 <= xx < m and 0 <= yy < n and ls[xx][yy] != '#'
                    and dis + 1 + 1000 * (1 + (i == 2)) <= dic_dis[(xx, yy, dx_, dy_)]):
                if dis + 1 + 1000 * (1 + (i == 2)) < dic_dis[(xx, yy, dx, dy)]:
                    dic_link[(xx, yy, dx_, dy_)] = {(x, y, dx, dy)}
                else:
                    dic_link[(xx, yy, dx_, dy_)].add((x, y, dx, dy))
                dic_dis[(xx, yy, dx_, dy_)] = dis + 1 + 1000 * (1 + (i == 2))
                heapq.heappush(queue, (dis + 1 + 1000 * (1 + (i == 2)), [xx, yy, (dx_, dy_)]))

    queue = [tuple(keep)]
    st_res = {(endx, endy)}
    st_res2 = {tuple(keep)}
    while queue:
        x, y, dx, dy = queue.pop(0)
        for newx, newy, newdx, newdy in dic_link[(x, y, dx, dy)]:
            if (newx, newy, newdx, newdy) not in st_res2:
                st_res.add((newx, newy))
                st_res2.add((newx, newy, newdx, newdy))
                queue.append((newx, newy, newdx, newdy))
    return res_dis, len(st_res)


if __name__ == "__main__":
    path1 = 'inputFull_20241216.txt'
    # path1 = 'inputPartial01_20241216.txt'
    ls = getList(path1)
    res1, res2 = check(ls)
    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
