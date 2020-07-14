from random import randint
from functools import reduce


def integer_array(n):
    i_a = []
    for i in range(1, n + 1):
        i_a.append(i)
    return i_a


def unsorted_array(a, b, l):
    u_a = []
    for i in range(l + 1):
        u_a.append(randint(a, b))
    return u_a


def list_duplicates_of(seq, item):
    start_at = -1
    indices = []
    while True:
        try:
            index = seq.index(item, start_at + 1)
        except ValueError:
            break
        else:
            indices.append(index)
            start_at = index
    return indices


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
