"""How do you find the missing number in a given integer array of 1 to 100?
"""
from common_functions import integer_array
from random import randrange

def sum_of_natural_num(n):
    return int(n * (n + 1) / 2)


def main():
    given_array = integer_array(100)
    given_array.remove(randrange(1, 101))
    # solution
    missing_number = sum_of_natural_num(100) - sum(given_array)
    print(given_array)
    print(missing_number)



if __name__ == "__main__":
    main()
