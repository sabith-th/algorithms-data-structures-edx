# uses python3
import math


def get_frequency(arr, elm):
    count = 0
    for e in arr:
        if e == elm:
            count += 1
    return count


def majority_element(arr):
    if (len(arr) <= 1):
        return arr[0]
    else:
        mid = math.floor(len(arr) / 2)
        left_major = majority_element(arr[:mid])
        right_major = majority_element(arr[mid:])
        if (left_major == right_major):
            return left_major
        left_major_count = get_frequency(arr, left_major)
        right_major_count = get_frequency(arr, right_major)
        if left_major_count > mid:
            return left_major
        elif right_major_count > mid:
            return right_major
        else:
            return -1


if __name__ == '__main__':
    inp = open("4_2_majority_element.in", "r")
    n = int(inp.readline())
    arr = [int(i) for i in inp.readline().split()]
    print(majority_element(arr))
