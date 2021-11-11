# Uses python3
import sys


def EuclidGCD(a, b):
    if b == 0:
        return a
    return EuclidGCD(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(EuclidGCD(a, b))
