# Uses python3
def calc_fib(n):
    arr = [0, 1]
    for x in range(2, n + 1):
        arr.append(arr[x - 1] + arr[x - 2])
    return arr[n]


n = int(input())
print(calc_fib(n))