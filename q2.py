"""How do you find the largest and smallest number in an unsorted integer array?
"""
from common_functions import unsorted_array



def main():
    given_array = unsorted_array(5,20,30)
    print(given_array)
    # solution
    given_array.sort()
    print(given_array)
    print("smallest number =", given_array[0])
    print("largest number =", given_array[-1])

if __name__ == "__main__":
    main()
