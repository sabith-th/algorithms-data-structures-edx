# uses python3


def eval(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return 0


def MinAndMax(i, j, op, m, M):
    mini = 100000
    maxi = -100000
    for k in range(i, j):
        a = eval(M[i][k], M[k + 1][j], op[k])
        b = eval(M[i][k], m[k + 1][j], op[k])
        c = eval(m[i][k], M[k + 1][j], op[k])
        d = eval(m[i][k], m[k + 1][j], op[k])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return (mini, maxi)


def get_maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset) + 1:2]
    n = len(d)
    #iniitializing matrices/tables
    m = [[0 for i in range(n)] for j in range(n)]  #minimized values
    M = [[0 for i in range(n)] for j in range(n)]  #maximized values
    for i in range(n):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, op, m, M)
    return M[0][n - 1]


if __name__ == "__main__":
    dataset = list('7+6+3-2-7-4*2+4+2-9*6*8')
    print(get_maximum_value(dataset))
