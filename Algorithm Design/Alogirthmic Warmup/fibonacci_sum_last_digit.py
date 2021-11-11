# Uses python3
import sys


def get_fibonacci(n):
    arr = [0, 1]
    for x in range(2, n + 1):
        arr.append(arr[x - 1] + arr[x - 2])
    return arr[n]


def fibonacci_sum_last_digit(n):
    rem = (get_fibonacci((n + 2) % 60) % 10)
    if (rem == 0):
        return 9
    else:
        return rem - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))
