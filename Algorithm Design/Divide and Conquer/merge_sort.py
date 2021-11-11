# uses python3
import math


def merge(B, C, m):
    D = []
    no_of_inversions = 0
    i = 0
    while (len(B) > 0 and len(C) > 0):
        b, c = B[0], C[0]
        if b <= c:
            D.append(b)
            B = B[1:]
            i += 1
        else:
            D.append(c)
            no_of_inversions = no_of_inversions + (m - i)
            C = C[1:]
    D.extend(B)
    D.extend(C)
    return (D, no_of_inversions)


def merge_sort(A):
    if (len(A) == 1):
        return (A, 0)
    m = math.floor(len(A) / 2)
    B, no_of_inversions_in_b = merge_sort(A[:m])
    C, no_of_inversions_in_c = merge_sort(A[m:])
    sortedA, no_of_inversions = merge(B, C, m)
    return (sortedA,
            no_of_inversions + no_of_inversions_in_b + no_of_inversions_in_c)


if __name__ == '__main__':
    inp = open("4_4_inversions.in", "r")
    n = int(inp.readline())
    arr = [int(i) for i in inp.readline().split()]
    sortedA, no_of_inversions = merge_sort(arr)
    print(no_of_inversions)
