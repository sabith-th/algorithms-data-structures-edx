# uses python3


def my_lcs(x_string, y_string):
    matrix = [[0 for each_x in range(0,
                                     len(y_string) + 1)]
              for each_y in range(0,
                                  len(x_string) + 1)]
    for each_y in range(len(y_string)):
        for each_x in range(len(x_string)):
            prev_x = each_x - 1
            prev_y = each_y - 1
            if (x_string[prev_x] == y_string[prev_y]):
                matrix[each_x][each_y] = matrix[prev_x][prev_y] + 1
            else:
                matrix[each_x][each_y] = max(matrix[prev_x][each_y],
                                             matrix[each_x][prev_y])
    return matrix[len(x_string) - 1][len(y_string) - 1]


if __name__ == "__main__":
    inp = open("test2.in", "r")
    m = int(inp.readline())
    X = [int(i) for i in inp.readline().split()]
    n = int(inp.readline())
    Y = [int(i) for i in inp.readline().split()]
    print(my_lcs(X, Y))
