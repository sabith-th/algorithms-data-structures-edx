# Uses python3
import sys


def pisano_period(m):
    a, b = 0, 1
    c = a + b
    for i in range(m * m):
        c = (a + b) % m
        a = b
        b = c
        if (a == 0 and b == 1):
            return i + 1


def get_fibonacci(n):
    arr = [0, 1]
    for x in range(2, n + 1):
        arr.append(arr[x - 1] + arr[x - 2])
    return arr[n]


def get_fibonacci_mod_m(n, m):
    if n <= 1:
        return n

    pi_m = pisano_period(m)
    return (get_fibonacci(n % pi_m) % m)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_mod_m(n, m))
