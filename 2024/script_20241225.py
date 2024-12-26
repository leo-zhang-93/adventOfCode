def get_list(path):
    """Reads a file and returns a list of lists of characters."""
    ls = []
    try:
        flag = 0
        tmp = []
        with open(path, 'r') as f:
            for line in f:
                if line == '\n':
                    ls.append(tmp)
                    tmp = []
                else:
                    tmp.append(list(line[:-1]))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []
    return ls

def processKey(grid):
    res = []
    for j in range(5):
        tmp_cnt = 0
        for i in range(5, 0, -1):
            if grid[i][j] == '#':
                tmp_cnt += 1
            else:
                break
        res.append(tmp_cnt)
    return res

def processLock(grid):
    res = []
    for j in range(5):
        tmp_cnt = 0
        for i in range(1, 6):
            if grid[i][j] == '#':
                tmp_cnt += 1
            else:
                break
        res.append(tmp_cnt)
    return res

def match(ls1, ls2):
    for i in range(5):
        if ls1[i] + ls2[i] <= 5:
            continue
        else:
            return False
    return True

def calc(ls):
    ls_keys = []
    ls_locks = []
    for grid in ls:
        if ''.join(grid[0]) == '#####':
            ls_locks.append(grid)
        elif ''.join(grid[-1]) == '#####':
            ls_keys.append(grid)

    ls_keys_processed = []
    ls_locks_processed = []
    for key in ls_keys:
        ls_keys_processed.append(processKey(key))
    for lock in ls_locks:
        ls_locks_processed.append(processLock(lock))

    result = 0
    for key_processed in ls_keys_processed:
        for lock_processed in ls_locks_processed:
            # print(key_processed, lock_processed)
            if match(key_processed, lock_processed):
                result += 1

    return result

if __name__ == "__main__":
    path1 = 'inputFull_20241225.txt'
    # path1 = 'inputPartial_20241224.txt'
    input_ls = get_list(path1)
    print(f"Part 1: {calc(input_ls)}")



