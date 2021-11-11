# Uses python3
import sys


def get_fibonacci_diff(m, n):
    k = max(m, n)
    arr = [0, 1]
    for x in range(2, k + 1):
        arr.append(arr[x - 1] + arr[x - 2])
    if (m > n):
        diff = arr[m] - arr[n]
    else:
        diff = arr[n] - arr[m - 1]
    return diff % 10


def fibonacci_partial_sum(from_, to):
    new_from = (from_ + 2) % 60
    new_to = (to + 2) % 60
    return get_fibonacci_diff(new_from, new_to)


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
