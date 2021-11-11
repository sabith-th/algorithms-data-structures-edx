# uses python3


def no_of_operations(n):
    cache = [0] * (n + 1)
    for i in range(1, n + 1):
        cache[i] = cache[i - 1] + 1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i // 2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i // 3] + 1)

    result = [1] * cache[-1]
    for i in range(1, cache[-1]):
        result[-i] = n
        if cache[n - 1] == cache[n] - 1:
            n -= 1
        elif n % 2 == 0 and (cache[n // 2] == cache[n] - 1):
            n //= 2
        else:  # n % 3 == 0 and (cache[n // 3] == cache[n] - 1):
            n //= 3
    return result


if __name__ == '__main__':
    print(no_of_operations(5))
