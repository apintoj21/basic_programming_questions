"""How do you find all pairs of an integer array whose sum is equal to a given number?
"""
from common_functions import list_duplicates_of


def pair_eq2_sum(array, pair_sum):
    a_map = {}
    # create the map
    for i, e in enumerate(array):
        a_map[e] = i
    # lookup
    for i, e in enumerate(array):
        if pair_sum - e in a_map:
            if e != pair_sum / 2:
                print("pair = {} and {}".format(array[i], array[a_map.get(pair_sum - e)]))

    l1 = list_duplicates_of(array, pair_sum / 2)
    if len(l1) > 1:
        for i in range(len(l1)):
            print("pair = {} and {}".format(int(pair_sum / 2), int(pair_sum / 2)))


def main():
    arr = [3, 4, 5, 4, 5]

    pair_eq2_sum(arr, 8)


if __name__ == "__main__":
    main()
