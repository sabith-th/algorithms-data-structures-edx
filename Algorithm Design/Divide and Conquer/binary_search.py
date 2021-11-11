# Uses python3
import math


def binary_search(A, low, high, key):
    while low <= high:
        mid = math.floor(low + (high - low) / 2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    inp = open("4_1_binary_search.in", "r")
    a, b = [], []
    a = [int(i) for i in inp.readline().split()]
    b = [int(i) for i in inp.readline().split()]
    n, k = a[0], b[0]
    a, b = a[1:], b[1:]
    count = 0
    for key in b:
        res = binary_search(a, 0, n - 1, key)
        if res != -1:
            count += 1
    print(count)
