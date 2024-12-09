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

def mirror(x1, y1, x2, y2):
    return [x2 - x1 + x2, y2 - y1 + y2, x1 - x2 + x1, y1 - y2 + y1]

def directions(x1, y1, x2, y2):
    return [x1 - x2, y1 - y2, x2 - x1, y2 - y1]

def calc1(ls):
    from collections import defaultdict
    dic = defaultdict(list)
    m, n = len(ls), len(ls[0])
    for i in range(m):
        for j in range(n):
            if ls[i][j] != '.':
                dic[ls[i][j]].append([i, j])
    st = set()
    for key in dic.keys():
        length = len(dic[key])
        for i in range(length - 1):
            x1, y1 = dic[key][i]
            for j in range(i + 1, length):
                x2, y2 = dic[key][j]
                xx1, yy1, xx2, yy2 = mirror(x1, y1, x2, y2)
                if 0 <= xx1 < m and 0 <= yy1 < n:
                    st.add((xx1, yy1))
                if 0 <= xx2 < m and 0 <= yy2 < n:
                    st.add((xx2, yy2))
    return len(st)


def calc2(ls):
    from collections import defaultdict
    dic = defaultdict(list)
    m, n = len(ls), len(ls[0])
    for i in range(m):
        for j in range(n):
            if ls[i][j] != '.':
                dic[ls[i][j]].append([i, j])
    st = set()
    for key in dic.keys():
        length = len(dic[key])
        for i in range(length - 1):
            x1, y1 = dic[key][i]
            st.add((x1, y1))
            for j in range(i + 1, length):
                x2, y2 = dic[key][j]
                st.add((x2, y2))
                dx1, dy1, dx2, dy2 = directions(x1, y1, x2, y2)
                xx1 = x1 + dx1
                yy1 = y1 + dy1
                while 0 <= xx1 < m and 0 <= yy1 < n:
                    st.add((xx1, yy1))
                    xx1 += dx1
                    yy1 += dy1
                xx2 = x2 + dx2
                yy2 = y2 + dy2
                while 0 <= xx2 < m and 0 <= yy2 < n:
                    st.add((xx2, yy2))
                    xx2 += dx2
                    yy2 += dy2
    return len(st)

if __name__ == "__main__":
    path1 = 'inputFull_20241208.txt'
    # path1 = 'inputPartial_20241208.txt'
    ls = getList(path1)

    # Part 1:
    print(calc1(ls))

    # Part 2:
    print(calc2(ls))