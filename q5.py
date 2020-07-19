"""How are duplicates removed from a given array while keeping the same order?
"""


def uniques(array):
    unique = set()
    return [x for x in array if not (x in unique or unique.add(x))]


def main():
    arr = [3, 4, 5, 4, 5, 6, 8, 7, 8, 9, 1, 2, 2, 4, 6, 7, 2]
    uniq = uniques(arr)
    print(uniq)


if __name__ == "__main__":
    main()
