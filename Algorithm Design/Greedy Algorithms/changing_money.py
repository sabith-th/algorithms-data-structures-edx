# Uses python3
import sys


def get_no_of_coins(n):
    no_of_coins = 0
    no_of_coins += int(n / 10)
    n = n % 10
    no_of_coins += int(n / 5)
    n = n % 5
    no_of_coins += n
    return no_of_coins


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_no_of_coins(n))
