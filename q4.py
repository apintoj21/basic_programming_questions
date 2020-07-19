"""How do you find duplicate numbers in an array if it contains multiple duplicates?
"""


def duplicates(array):
    unique = set()
    return {x for x in array if x in unique or unique.add(x)}


def main():
    arr = [3, 4, 5, 4, 5, 6, 8, 7, 8, 9, 1, 2, 2, 4, 6, 7, 2]
    dup = duplicates(arr)
    print(dup)


if __name__ == "__main__":
    main()
