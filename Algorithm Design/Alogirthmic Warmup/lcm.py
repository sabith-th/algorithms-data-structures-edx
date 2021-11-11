# Uses python3
import sys


def EuclidGCD(a, b):
    if b == 0:
        return a
    return EuclidGCD(b, a % b)


def LCM(a, b):
    gcd = EuclidGCD(a, b)
    c = int(a / gcd)
    return c * b


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(LCM(a, b))
