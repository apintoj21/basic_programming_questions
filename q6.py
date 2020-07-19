"""Quicksort In-place"""
from common_functions import unsorted_array


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort_inplace(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        idx = partition(array, low, high)
        quicksort_inplace(array, low, idx-1)
        quicksort_inplace(array, idx+1, high)


def main():
    arr = unsorted_array(0, 50, 10)
    print("Unsorted = ", arr)
    quicksort_inplace(arr)
    print("Sorted = ", arr)


if __name__ == "__main__":
    main()
