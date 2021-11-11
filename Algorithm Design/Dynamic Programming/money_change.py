# uses python3
import math


def dpChange(money, coins):
    minNumCoins = [0] * (money + 1)
    for m in range(1, money + 1):
        minNumCoins[m] = math.inf
        for i in coins:
            if m >= i:
                numCoins = minNumCoins[m - i] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    return minNumCoins[money]


if __name__ == '__main__':
    print(dpChange(950, [1, 3, 4]))
