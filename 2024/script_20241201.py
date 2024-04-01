"""
This script reads a text file containing pairs of integers, parses the data,
sorts the integers, and performs calculations on the sorted lists.

Args:
    path (str): The path to the input file.

Returns:
    tuple: A tuple containing two sorted lists of integers.
"""
def calc1(path):
    """Reads and parses the input file, returning sorted lists.

    Args:
        path (str): The path to the input file.

    Returns:
        tuple: A tuple containing two sorted lists of integers.
    """

    ls1: list[Any] = []
    ls2: list[Any] = []

    try:
        with open(path, 'r') as f:
            for line in f:
                val1, val2 = map(int, line[:-1].split('   '))
                ls1.append(val1)
                ls2.append(val2)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return [], []
    except ValueError:
        print(f"Invalid input format in {path}")
        return [], []

    return ls1, ls2


if __name__ == "__main__":
    # path1 = 'inputPartial_20241201.txt'
    path1 = 'inputFull_20241201.txt'
    ls1, ls2 = calc1(path1)
    ls1 = sorted(ls1)
    ls2 = sorted(ls2)

    # ... further processing of ls1 and ls2 ...
    # For example, the calculations from your original code:

    # Part 1:
    n = len(ls1)
    print(sum([abs(ls1[i] - ls2[i]) for i in range(n)]))

    # Part 2:
    from collections import Counter

    res = 0
    counter1 = Counter(ls1)
    counter2 = Counter(ls2)
    for key in counter1.keys():
        res += key * counter1[key] * counter2[key]
    print(res)
