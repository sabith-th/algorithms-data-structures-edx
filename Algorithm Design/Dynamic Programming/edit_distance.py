# uses python3


def edit_distance(A, B):
    m, n = len(A), len(B)
    D = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                D[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                D[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                D[i][j] = 1 + min(
                    D[i][j - 1],  # Insert 
                    D[i - 1][j],  # Remove 
                    D[i - 1][j - 1])
    return D[m][n]


if __name__ == "__main__":
    inp = open("5_3_edit_distance.in", "r")
    A = list(inp.readline())
    B = list(inp.readline())
    A.pop()
    print(edit_distance(A, B))
