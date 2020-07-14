from random import randint


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
