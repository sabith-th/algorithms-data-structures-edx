# Uses python3

if __name__ == '__main__':
    inp = open("3_3_dot_product.in", "r")
    n, a, b = 0, [], []
    n = int(inp.readline())
    a = [int(i) for i in inp.readline().split()]
    b = [int(i) for i in inp.readline().split()]
    a.sort()
    b.sort()
    product = 0
    for i in range(n):
        product = product + (a[i] * b[i])
    print(product)
