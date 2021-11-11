# uses python3


# Returns length of LCS
# for X[0..m-1], Y[0..n-1]
# and Z[0..o-1]
def lcsOf3(X, Y, Z, m, n, o):

    L = [[[0 for i in range(o + 1)] for j in range(n + 1)]
         for k in range(m + 1)]
    ''' Following steps build L[m+1][n+1][o+1] in 
    bottom up fashion. Note that L[i][j][k] 
    contains length of LCS of X[0..i-1] and 
    Y[0..j-1] and Z[0.....k-1] '''
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0

                elif (X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1

                else:
                    L[i][j][k] = max(
                        max(L[i - 1][j][k], L[i][j - 1][k]), L[i][j][k - 1])

    # L[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]


if __name__ == "__main__":
    inp = open("5_5_lcs3.in", "r")
    m = int(inp.readline())
    X = [int(i) for i in inp.readline().split()]
    n = int(inp.readline())
    Y = [int(i) for i in inp.readline().split()]
    o = int(inp.readline())
    Z = [int(i) for i in inp.readline().split()]
    print(lcsOf3(X, Y, Z, m, n, o))
